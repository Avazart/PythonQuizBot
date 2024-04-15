import asyncio
import logging
import re

from aiogram import Bot, F, Router, html
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Document, LinkPreviewOptions, Message
from sqlalchemy.ext.asyncio import AsyncSession

from ...bot.types import (
    Action,
    BackData,
    BotContext,
    CloseData,
    FinishUploadingData,
    Form,
    MoreResultsData,
    QuizData,
    ResultData,
)
from ...database.models import Quiz
from ...database.utils.quiz_results_ import find_user_results, get_result
from ...database.utils.quizzes import delete_quiz, find_quiz, get_quiz_info
from ...quiz_parser import from_file, get_last_modified
from ...settings import RESULT_COUNT
from ...utils.quiz_utils import (
    download_quiz,
    fmt_result,
    generate_file_path,
    load_quiz,
    make_quiz_info_text,
    save_quiz,
    show_files,
    upload_quiz,
)
from ..keyboards.keyboard import (
    finish_uploading_keyboard,
    quiz_tool_keyboard,
    result_keyboard,
)
from ..pages import (
    PageId,
    PageItemData,
    PageShowData,
    files_page,
    manage_quizzes_page,
    users_page,
)

logger = logging.getLogger(__name__)
router = Router()


# FILES


@router.message(Command(commands=["files"]))
async def files_command(
    message: Message,
    state: FSMContext,
    context: BotContext,
    session: AsyncSession,
):
    files: dict[str, tuple] = {}
    for i, path in enumerate(context.settings.quiz_folder.glob("*.py")):
        if m := re.match(r"^(\d+)\.\s*(.*)", path.stem):
            quiz_id = int(m.group(1))
            name = m.group(2)
        else:
            quiz_id = None
            name = path.stem

        quiz: Quiz | None = None
        if quiz_id is not None:
            if quiz_info := await get_quiz_info(quiz_id, session):
                quiz, _ = quiz_info
        if not quiz:
            quiz = await find_quiz(name, session)

        if (not quiz) or (get_last_modified(path) > quiz.last_modified):
            files[str(i)] = name, path.name, quiz_id, bool(quiz)

    logger.debug(files)
    await state.set_data(dict(files=files))
    await files_page.show(message, 0, False, files=files)


@router.callback_query(
    PageShowData.filter(F.id == PageId.FILES),
    F.message.as_("message"),
)
async def handle_show_files(
    _: CallbackQuery,
    message: Message,
    callback_data: PageShowData,
    state: FSMContext,
):
    data = await state.get_data()
    if files := data.get("files"):
        await files_page.show(message, callback_data.offset, True, files=files)


@router.callback_query(
    PageItemData.filter(F.id == PageId.FILES),
    F.message.as_("message"),
)
async def handle_file_data(
    query: CallbackQuery,
    message: Message,
    callback_data: PageItemData,
    state: FSMContext,
    context: BotContext,
    session: AsyncSession,
):
    data = await state.get_data()
    if not (files := data.get("files")):
        return

    if (file_info := files.get(str(callback_data.item_id))) is None:
        return

    name, file_name, quiz_id, exist = file_info
    file_path = context.settings.quiz_folder / file_name
    async with session.begin():
        try:
            if exist:
                await delete_quiz(quiz_id, session)
            new_quiz = from_file(file_path, file_name, name)
            if quiz_id is not None:
                new_quiz.id = quiz_id
            session.add(new_quiz)
            await query.answer("Successful!")
            await show_files(message, state, context, session, edit=True)
        except Exception as e:
            await message.answer(f'{e!r}: "{e}"')


@router.message(
    Form.ADD_SOURCE,
    F.content_type == ContentType.DOCUMENT,
    F.document.as_("document"),
)
async def handle_file(
    message: Message,
    document: Document,
    context: BotContext,
    bot: Bot,
    session: AsyncSession,
):
    try:
        file_id = document.file_id
        assert document.file_name
        local_path = generate_file_path(
            document.file_name,
            context.settings.quiz_folder,
        )
        file = await bot.get_file(file_id)
        file_path = file.file_path
        assert file_path
        await bot.download_file(file_path, local_path)
        await message.answer(
            f"Successful uploaded! File: {html.code(local_path.name)}",
            reply_markup=finish_uploading_keyboard(),
            parse_mode=ParseMode.HTML,
        )
        async with session.begin():
            quiz = load_quiz(local_path.name, context)
            session.add(quiz)
        await message.answer("Successful added to database!")
    except Exception as e:
        await message.answer(
            f'{e!r}: "{e}"',
            reply_markup=finish_uploading_keyboard(),
        )


# QUIZZES


@router.message(Command(commands=["manage_quizzes"]))
async def manage_quizzes_command(message: Message, session: AsyncSession):
    await manage_quizzes_page.show(message, 0, False, session=session)


@router.callback_query(
    PageShowData.filter(F.id == PageId.MANAGE_QUIZZES),
    F.message.as_("message"),
)
async def handle_show_quizzes(
    _: CallbackQuery,
    message: Message,
    callback_data: PageShowData,
    session: AsyncSession,
):
    await manage_quizzes_page.show(
        message,
        callback_data.offset,
        True,
        session=session,
    )


@router.callback_query(
    PageItemData.filter(F.id == PageId.MANAGE_QUIZZES),
    F.message.as_("message"),
)
async def handle_manage_quiz(
    query: CallbackQuery,
    message: Message,
    callback_data: PageItemData,
    session: AsyncSession,
):
    if quiz_info := await get_quiz_info(callback_data.item_id, session):
        text = make_quiz_info_text(quiz_info.quiz, quiz_info.question_count)
        markup = quiz_tool_keyboard(quiz_info.quiz)
        await message.edit_text(text, reply_markup=markup)
    else:
        await query.answer("Quiz not found!")


@router.callback_query(
    QuizData.filter(F.action == Action.DELETE),
    F.message.as_("message"),
)
async def handle_delete_quiz(
    _: CallbackQuery,
    message: Message,
    callback_data: QuizData,
    session: AsyncSession,
):
    async with session.begin():
        await delete_quiz(callback_data.id, session)
    await manage_quizzes_page.show(message, 0, True, session=session)


@router.callback_query(
    QuizData.filter(F.action == Action.UPDATE),
    F.message.as_("message"),
)
async def handle_update_quiz(
    query: CallbackQuery,
    message: Message,
    callback_data: QuizData,
    context: BotContext,
    session: AsyncSession,
):
    async with session.begin():
        try:
            if old_quiz_info := await get_quiz_info(callback_data.id, session):
                new_quiz = load_quiz(old_quiz_info.quiz.source, context)
                session.add(new_quiz)
                await delete_quiz(callback_data.id, session)
                await message.answer("Successful!")
            else:
                await query.answer("Quiz not found!")
        except Exception as e:
            await message.answer(f'{e!r}: "{e}"')

    await manage_quizzes_page.show(message, 0, True, session=session)


@router.callback_query(
    QuizData.filter(F.action == Action.DOWNLOAD),
    F.message.as_("message"),
)
async def handle_download_quiz(
    query: CallbackQuery,
    message: Message,
    callback_data: QuizData,
    context: BotContext,
    session: AsyncSession,
):
    try:
        db_quiz_info = await get_quiz_info(callback_data.id, session)
        if not db_quiz_info:
            return
        if remote_quiz := download_quiz(db_quiz_info.quiz.source, context):
            file_path = generate_file_path(
                remote_quiz.name,
                context.settings.quiz_folder,
            )
            save_quiz(file_path, remote_quiz)
            await message.answer(
                "Successful saved!\nUse {} for add quiz".format(
                    html.code(f"/add {file_path.name}")
                ),
                parse_mode=ParseMode.HTML,
            )
        else:
            await query.answer("Quiz not found!")
    except Exception as e:
        await message.answer(f'{e!r}: "{e}"')
    await manage_quizzes_page.show(message, 0, True, session=session)


@router.callback_query(
    QuizData.filter(F.action == Action.UPLOAD),
    F.message.as_("message"),
)
async def handle_upload_quiz(
    _: CallbackQuery,
    message: Message,
    callback_data: QuizData,
    context: BotContext,
    session: AsyncSession,
):
    try:
        db_quiz_info = await get_quiz_info(callback_data.id, session)
        if not db_quiz_info:
            return
        page_url = upload_quiz(db_quiz_info.quiz.source, context)
        logger.debug(page_url)
        await message.answer(
            "Successful uploaded!\nUse {} for add quiz".format(
                html.code(f"/add {page_url}")
            ),
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        await message.answer(f'{e!r}: "{e}"')
    await manage_quizzes_page.show(message, 0, True, session=session)


@router.callback_query(
    QuizData.filter(F.action == Action.RENAME),
    F.message.as_("message"),
)
async def handle_rename_quiz(
    _: CallbackQuery,
    message: Message,
    callback_data: QuizData,
    state: FSMContext,
):
    await state.set_state(Form.RENAME_QUIZ)
    await state.set_data(dict(quiz_id=callback_data.id))
    await message.answer("Enter the new quiz name:")
    await message.delete()


@router.message(Form.RENAME_QUIZ, F.text.as_("text"))
async def handle_enter_name(
    message: Message,
    text: str,
    state: FSMContext,
    session: AsyncSession,
):
    data = await state.get_data()
    await state.clear()

    quiz_id = data["quiz_id"]
    async with session.begin():
        if quiz_info := await get_quiz_info(quiz_id, session):
            quiz_info.quiz.name = text.strip()
        else:
            await message.answer("Quiz not found!")
    await manage_quizzes_page.show(message, 0, True, session=session)


# RESULTS


@router.callback_query(ResultData.filter(), F.message.as_("message"))
async def handle_result(
    _: CallbackQuery,
    message: Message,
    callback_data: ResultData,
    session: AsyncSession,
):
    if result := await get_result(callback_data.id, session):
        text = fmt_result(result)
        await message.answer(
            text,
            link_preview_options=LinkPreviewOptions(is_disabled=True),
            parse_mode=ParseMode.HTML,
        )


@router.callback_query(
    BackData.filter(),
    F.message.as_("message"),
)
async def handle_back(
    _: CallbackQuery,
    message: Message,
    session: AsyncSession,
):
    await manage_quizzes_page.show(message, 0, True, session=session)


# USERS


@router.message(Command(commands=["users"]))
async def users_command(message: Message, session: AsyncSession):
    await users_page.show(message, 0, False, session=session)


@router.callback_query(
    PageShowData.filter(F.id == PageId.USERS),
    F.message.as_("message"),
)
async def handle_show_users(
    _: CallbackQuery,
    message: Message,
    callback_data: PageShowData,
    session: AsyncSession,
):
    await users_page.show(message, callback_data.offset, True, session=session)


@router.callback_query(MoreResultsData.filter(), F.message.as_("message"))
@router.callback_query(
    PageItemData.filter(F.id == PageId.USERS),
    F.message.as_("message"),
)
async def handle_user(
    _: CallbackQuery,
    message: Message,
    callback_data: PageItemData | MoreResultsData,
    session: AsyncSession,
):
    if isinstance(callback_data, PageItemData):
        offset = 0
        user_id = callback_data.item_id
    else:
        offset = callback_data.offset
        user_id = callback_data.id

    if results := await find_user_results(
        user_id,
        offset,
        RESULT_COUNT + 1,
        session,
    ):
        for i, result in enumerate(results[:RESULT_COUNT]):
            text = (
                f"#{result.quiz_id} "
                f"{result.quiz.name} "
                f"[{result.created_at}]"
            )
            if (i == RESULT_COUNT - 1) and (len(results) > RESULT_COUNT):
                more_offset = offset + RESULT_COUNT
            else:
                more_offset = None
            markup = result_keyboard(user_id, result.id, more_offset)
            await message.answer(text, reply_markup=markup)
            await asyncio.sleep(0.2)
    else:
        await message.answer("No quiz results!")


# ADD SOURCE


@router.message(Command(commands=["add"]))
async def add_command(
    message: Message,
    state: FSMContext,
    command: CommandObject,
    context: BotContext,
    session: AsyncSession,
):
    if source := command.args:
        try:
            async with session.begin():
                quiz = load_quiz(source, context)
                session.add(quiz)
            await message.answer("Successful!")
            await manage_quizzes_page.show(message, 0, False, session=session)
        except Exception as e:
            await message.answer(f'{e!r}: "{e}"')
    else:
        await state.set_state(Form.ADD_SOURCE)
        await message.answer("Enter source or send quiz file:")


@router.message(Form.ADD_SOURCE, F.text.as_("text"))
async def handle_enter_source(
    message: Message,
    text: str,
    state: FSMContext,
    context: BotContext,
    session: AsyncSession,
):
    try:
        async with session.begin():
            quiz = load_quiz(text, context)
            session.add(quiz)
        await message.answer("Successful!")
        await manage_quizzes_page.show(message, 0, True, session=session)
    except Exception as e:
        await message.answer(f'{e!r}: "{e}"')
    await state.clear()


@router.callback_query(
    Form.ADD_SOURCE,
    FinishUploadingData.filter(),
    F.message.as_("message"),
)
async def handle_finish_uploading(
    _: CallbackQuery,
    message: Message,
    state: FSMContext,
    session: AsyncSession,
):
    await state.clear()
    await manage_quizzes_page.show(message, 0, True, session=session)


# CLOSE  files, quizzes


@router.callback_query(CloseData.filter(), F.message.as_("message"))
async def handle_close(_: CallbackQuery, message: Message):
    await message.delete()
