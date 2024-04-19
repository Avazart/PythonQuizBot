import logging

from aiogram import F, Router
from aiogram.enums import ChatType, ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, LinkPreviewOptions, Message, User
from sqlalchemy.ext.asyncio import AsyncSession

from ...database.models import SingleAnswer
from ...database.utils.answers import find_single_answers
from ...database.utils.questions import find_question
from ...utils.quiz_utils import check_option, make_answer_text, show_question
from ..keyboards.keyboard import main_keyboard
from ..pages import PageCloseData, PageId, PageShowData, select_quizzes_page
from ..types import ApplyData, Form, OptionData

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)
router.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)


@router.message(Command(commands=["start"]), F.from_user.as_("from_user"))
async def start_command(
    message: Message,
    state: FSMContext,
    command: CommandObject,
    session: AsyncSession,
):
    await state.clear()
    if not command.args:
        await message.answer("Main menu", reply_markup=main_keyboard())
        return
    try:
        quiz_id, q_n, group_id, message_id = map(
            int, command.args.split("_", maxsplit=3)
        )
        if question := await find_question(quiz_id, q_n, session):
            await show_question(
                question,
                answer=[],
                edit=False,
                single=True,
                message=message,
            )
            await state.set_state(Form.SINGLE_QUESTION)
            await state.update_data(
                group_id=group_id,
                message_id=message_id,
                answers={},
            )
        else:
            await message.answer("Sorry, but the qustion is not exist!")
    except ValueError:
        await message.answer("Wrong start params")


@router.callback_query(
    Form.SINGLE_QUESTION,
    OptionData.filter(),
    F.message.as_("message"),
)
async def handle_option(
    _: CallbackQuery,
    message: Message,
    callback_data: OptionData,
    state: FSMContext,
    session: AsyncSession,
):
    await check_option(callback_data, True, message, state, session)


@router.callback_query(
    Form.SINGLE_QUESTION,
    ApplyData.filter(),
    F.message.as_("message"),
    F.from_user.as_("from_user"),
)
async def handle_apply(
    _: CallbackQuery,
    message: Message,
    from_user: User,
    callback_data: ApplyData,
    state: FSMContext,
    session: AsyncSession,
):
    async with session.begin():
        if q := await find_question(
            callback_data.quiz_id,
            callback_data.q_n,
            session,
        ):
            data = await state.get_data()
            answers = data.get("answers", {})
            group_id = data["group_id"]
            message_id = data["message_id"]
            answer = answers.get(str(q.n), [])
            correct, text = make_answer_text(q, answer)

            if not await find_single_answers(
                group_id,
                message_id,
                from_user.id,
                session,
            ):
                for option_id in answer:
                    single = SingleAnswer(
                        group_id=group_id,
                        message_id=message_id,
                        user_id=from_user.id,
                        option_id=option_id,
                    )
                    session.add(single)

            await message.edit_reply_markup(reply_markup=None)
            await state.clear()
            await message.edit_text(
                text,
                link_preview_options=LinkPreviewOptions(is_disabled=True),
                parse_mode=ParseMode.HTML,
            )


@router.message(F.text == "Quizzes")
async def handle_main_menu(message: Message, session: AsyncSession):
    await select_quizzes_page.show(message, 0, False, session=session)


@router.callback_query(
    PageShowData.filter(F.id == PageId.SELECT_QUIZZES),
    F.message.as_("message"),
)
async def handle_show_quizzes(
    _: CallbackQuery,
    message: Message,
    callback_data: PageShowData,
    session: AsyncSession,
):
    await select_quizzes_page.show(
        message,
        callback_data.offset,
        True,
        session=session,
    )


@router.callback_query(PageCloseData.filter(), F.message.as_("message"))
async def handle_close_page(_: CallbackQuery, message: Message):
    await message.delete()
