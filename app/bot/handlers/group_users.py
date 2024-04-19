import itertools
import logging
import random
from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.enums import ChatType, ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import (
    CallbackQuery,
    Chat,
    Message,
    ReplyKeyboardRemove,
)
from sqlalchemy.ext.asyncio import AsyncSession

from ...database.utils.answers import find_single_answers
from ...database.utils.questions import get_options
from ...database.utils.quizzes import get_quizzes_info
from ...utils.quiz_utils import show_question_in_group
from ..keyboards.keyboard import update_results_keyboard
from ..middlewares.group_middlewares import GroupMiddleware
from ..types import CloseData, UpdateResultsData

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(F.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP)))
router.callback_query.filter(
    F.message.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP))
)
router.message.middleware(GroupMiddleware())
router.callback_query.middleware(GroupMiddleware())


@router.message(Command(commands=["hide"]))
async def hide_command(message: Message):
    await message.answer("-", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=["quiz"]))
async def quiz_command(
    message: Message,
    command: CommandObject,
    session: AsyncSession,
    bot: Bot,
):
    if not (quizzes := await get_quizzes_info(0, None, session)):
        await message.answer("No quizzes!")
        return

    if args := command.args and command.args.split():
        try:
            quiz_id = int(args[0])
            quiz, count = next(
                ((qz, count) for qz, count in quizzes if qz.id == quiz_id)
            )
            q_n = int(args[1]) if len(args) >= 2 else random.randint(1, count)
        except (ValueError, TypeError):
            await message.answer("Wrong arguments!")
            return
        except StopIteration:
            await message.answer("Quiz not found!")
            return
    else:
        quiz, count = random.choice(quizzes)
        q_n = random.randint(1, count)

    logger.debug(f"{quiz.id=} {quiz.id=} {count=}")

    await show_question_in_group(quiz.id, q_n, session, message, bot)


@router.message(
    Command(commands=["results"]),
    F.reply_to_message.as_("reply_to_message"),
    F.chat.as_("chat"),
)
async def results_command(
    message: Message,
    reply_to_message: Message,
    chat: Chat,
    session: AsyncSession,
):
    if answers := await find_single_answers(
        chat.id,
        reply_to_message.message_id,
        None,
        session,
    ):
        question_id = answers[0].option.question_id
        options = await get_options(question_id, session)
        correct = {option.id for option in options if option.correct}
        lines = []
        g = itertools.groupby(answers, key=lambda a: a.user_id)
        for _, answer in g:
            user_opts = list(answer)
            user = user_opts[0].user.as_aiogram_user()
            opt_ids = {a.option_id for a in user_opts}
            ch = "👍" if opt_ids == correct else "👎"
            lines.append(f"{user.mention_html()} {ch}")
        await reply_to_message.reply(
            text="\n".join(lines),
            parse_mode=ParseMode.HTML,
            reply_markup=update_results_keyboard(reply_to_message.message_id),
        )
    else:
        await message.answer(
            "No results, yet!",
            reply_markup=update_results_keyboard(reply_to_message.message_id),
        )


@router.callback_query(
    UpdateResultsData.filter(),
    F.message.as_("message"),
    F.message.chat.as_("chat"),
)
async def handle_update_results(
    _: CallbackQuery,
    message: Message,
    chat: Chat,
    callback_data: UpdateResultsData,
    session: AsyncSession,
):
    if answers := await find_single_answers(
        chat.id,
        callback_data.message_id,
        None,
        session,
    ):
        question_id = answers[0].option.question_id
        options = await get_options(question_id, session)
        correct = {option.id for option in options if option.correct}
        lines = []
        g = itertools.groupby(answers, key=lambda a: a.user_id)
        for _, answer in g:
            user_opts = list(answer)
            user = user_opts[0].user.as_aiogram_user()
            opt_ids = {a.option_id for a in user_opts}
            ch = "👍" if opt_ids == correct else "👎"
            lines.append(f"{user.mention_html()} {ch}")
        lines.append(f"\nLast update: {datetime.now():%H:%M:%S}")
        await message.edit_text(
            text="\n".join(lines),
            parse_mode=ParseMode.HTML,
            reply_markup=update_results_keyboard(callback_data.message_id),
        )
    else:
        lines = [
            "No results, yet!",
            "",
            f"Last update: {datetime.now():%H:%M:%S}",
        ]
        await message.edit_text(
            text="\n".join(lines),
            reply_markup=update_results_keyboard(callback_data.message_id),
        )


@router.callback_query(CloseData.filter(), F.message.as_("message"))
async def handle_close(_: CallbackQuery, message: Message):
    await message.delete()
