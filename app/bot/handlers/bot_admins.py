import asyncio
import logging
from pathlib import Path
from typing import BinaryIO

from aiogram import Bot, F, Router
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    BufferedInputFile,
    CallbackQuery,
    Chat,
    Document,
    LinkPreviewOptions,
    Message,
)
from sqlalchemy.ext.asyncio import AsyncSession

from ...bot.types import (
    Action,
    BackData,
    BotContext,
    CloseData,
    Form,
    MoreResultsData,
    QuizData,
    ResultData,
    StopUploadingData,
)
from ...database.utils.quiz_results import find_user_results, get_result
from ...database.utils.quizzes import (
    delete_quiz,
    find_quiz,
    get_quiz_info,
    get_quizzes,
)
from ...quiz_parser import from_file, from_text
from ...settings import RESULT_COUNT
from ...utils.aux_utils import send_parts
from ...utils.quiz_utils import (
    fmt_result,
    make_quiz_info_text,
    normalize_file_name,
    parse_file_path,
    quiz_as_text,
    scan_files,
)
from ..keyboards.keyboard import (
    quiz_tool_keyboard,
    result_keyboard,
    stop_uploading_keyboard,
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
    files = await scan_files(context.settings.quiz_folder, session)
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
            await query.answer("Successs!")

            files = await scan_files(context.settings.quiz_folder, session)
            await state.set_data(dict(files=files))
            await files_page.show(message, 0, True, files=files)
        except Exception as e:
            await message.answer(f'{e!r}: "{e}"')


# MANAGE QUIZZES


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


# DELETE QUIZ


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


# UPLOAD QUIZ FILES


@router.message(Command(commands=["upload"]))
async def upload_command(message: Message, state: FSMContext):
    await state.set_state(Form.UPLOAD)
    markup = stop_uploading_keyboard()
    await message.answer("Upload files:", reply_markup=markup)


@router.callback_query(
    Form.UPLOAD,
    StopUploadingData.filter(),
    F.message.as_("message"),
)
async def handle_uploading_files(
    _: CallbackQuery,
    message: Message,
    state: FSMContext,
    session: AsyncSession,
):
    await state.clear()
    await manage_quizzes_page.show(message, 0, True, session=session)


@router.message(
    Form.UPLOAD,
    F.content_type == ContentType.DOCUMENT,
    F.document.as_("document"),
)
async def handle_file(
    message: Message,
    document: Document,
    bot: Bot,
    session: AsyncSession,
):
    assert document.file_name
    try:
        quiz_id, name = parse_file_path(Path(document.file_name))
        if quiz_id is None:
            if quiz := await find_quiz(name, session):
                quiz_id = quiz.id

        file = await bot.get_file(document.file_id)
        assert file.file_path

        buffer: BinaryIO | None = await bot.download_file(file.file_path)
        assert buffer

        content = buffer.read()
        text = content.decode("utf-8")
        quiz = from_text(text, normalize_file_name(document.file_name), name)

        # Add to database
        async with session.begin():
            if quiz_id is not None:
                await delete_quiz(quiz_id, session)
                quiz.id = quiz_id
            session.add(quiz)

        await message.answer(f'Quiz "{name}" successful added to database!')
    except Exception as e:
        await message.answer(f'{e!r}: "{e}"')


# DOWNLOAD QUIZ


@router.callback_query(
    QuizData.filter(F.action == Action.DOWNLOAD),
    F.message.chat.as_("chat"),
)
async def handle_downoad_quiz(
    _: CallbackQuery,
    chat: Chat,
    callback_data: QuizData,
    session: AsyncSession,
    bot: Bot,
):
    if quiz_info := await get_quiz_info(callback_data.id, session, True):
        text = quiz_as_text(quiz_info.quiz)
        buffer_file = BufferedInputFile(
            file=text.encode("utf-8"),
            filename=quiz_info.quiz.source,
        )
        await bot.send_document(chat.id, buffer_file)


@router.message(Command(commands=["download_all"]), F.chat.as_("chat"))
async def download_all_command(
    _: Message,
    chat: Chat,
    session: AsyncSession,
    bot: Bot,
):
    quizzes = await get_quizzes(0, None, session)
    for quiz in quizzes:
        text = quiz_as_text(quiz)
        buffer_file = BufferedInputFile(
            file=text.encode("utf-8"),
            filename=quiz.source,
        )
        await bot.send_document(chat.id, buffer_file)
        await asyncio.sleep(0.2)


# RESULTS


@router.callback_query(ResultData.filter(), F.message.as_("message"))
async def handle_result(
    _: CallbackQuery,
    message: Message,
    callback_data: ResultData,
    session: AsyncSession,
):
    if result := await get_result(callback_data.id, session):
        parts = fmt_result(result)
        kwargs = dict(
            link_preview_options=LinkPreviewOptions(is_disabled=True),
            parse_mode=ParseMode.HTML,
        )
        await send_parts(message, parts, sep="\n\n", **kwargs)


@router.callback_query(BackData.filter(), F.message.as_("message"))
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


# CLOSE  files, quizzes


@router.callback_query(CloseData.filter(), F.message.as_("message"))
async def handle_close(_: CallbackQuery, message: Message):
    await message.delete()
