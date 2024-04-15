import logging
import re
from pathlib import Path

from aiogram import Bot, html
from aiogram.enums import ParseMode, PollType
from aiogram.fsm.context import FSMContext
from aiogram.types import LinkPreviewOptions, Message
from aiogram.utils.deep_linking import create_start_link
from notion_client import Client
from sqlalchemy.ext.asyncio import AsyncSession

from ..bot.keyboards.keyboard import (
    question_keyboard,
)
from ..bot.pages import files_page
from ..bot.types import BotContext, OptionData
from ..database.models import Quiz, QuizResult
from ..database.utils.questions import find_question
from ..database.utils.quizzes import find_quiz, get_quiz_info
from ..notion_utils.utils import (
    export_to_notion,
    import_from_notion,
    parse_page_id,
)
from ..quiz_parser import Question, from_file, get_last_modified
from ..settings import FILE_COUNT

logger = logging.getLogger(__name__)


def fmt_question(question: Question, quiz_id: int | None = None):
    if quiz_id is None:
        lines = [f"{html.bold(str(question.n))}. {question.text}"]
    else:
        lines = [f"{html.bold(f'{quiz_id}.{question.n}')}. {question.text}"]
    if question.code:
        lines.append(html.pre_language(html.unparse(question.code), "python"))
    if question.link:
        lines.append(
            " ".join(
                html.link(f"[{i}]", question.link)
                for i, link in enumerate(
                    filter(None, question.link.split()), 1
                )
            )
        )
    return "\n".join(lines)


async def show_question(
    question: Question,
    answer: list[int],
    edit: bool,
    single: bool,
    message: Message,
) -> None:
    markup = question_keyboard(question, answer, single)
    method = "edit_text" if edit else "answer"
    await getattr(message, method)(
        text=fmt_question(question),
        reply_markup=markup,
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        parse_mode=ParseMode.HTML,
    )


def make_quiz_info_text(quiz: Quiz, count: int) -> str:
    return f"{quiz.name} ({count}) [{quiz.last_modified:%H:%M %d.%m.%y}]"


def load_quiz(source: str, context: BotContext) -> Quiz:
    if page_id := parse_page_id(source):
        token = context.settings.notion_token.get_secret_value()
        client = Client(auth=token)
        quiz = import_from_notion(page_id, source, client)
    else:
        path = context.settings.quiz_folder / source
        quiz = from_file(path, source, path.stem)
    return quiz


def download_quiz(source: str, context: BotContext) -> Quiz | None:
    if page_id := parse_page_id(source):
        token = context.settings.notion_token.get_secret_value()
        client = Client(auth=token)
        quiz = import_from_notion(page_id, source, client)
        return quiz
    return None


def upload_quiz(source: str, context: BotContext) -> str:
    token = context.settings.notion_token.get_secret_value()
    client = Client(auth=token)
    file_path = context.settings.quiz_folder / source
    parent_id = context.settings.notion_parent_pade_id
    page_url = export_to_notion(file_path, parent_id, client)
    return page_url


def normalize_file_name(text: str) -> str:
    return re.sub(r'[/\\:*?"<>|]', "_", text)


def generate_file_path(name: str, folder: Path) -> Path:
    name = normalize_file_name(name).removesuffix(".py")
    n = 1
    while True:
        file_name = f"{name} ({n})" if n > 1 else name
        logger.debug(file_name)
        file_path = (folder / file_name).with_suffix(".py")
        if not file_path.exists():
            return file_path
        n += 1
        logger.debug((file_path, n))


def save_quiz(file_path: Path, quiz: Quiz):
    with file_path.open("w", encoding="utf-8") as file:
        for n, question in enumerate(quiz.questions, 1):
            print(f"# # {n:=<75}", end="\n\n", file=file)
            print(f"# ? {question.text}", end="\n\n", file=file)
            if question.code:
                print(question.code, end="\n\n", file=file)

            for option in question.options:
                ch = "+" if option.correct else "-"
                print(f"# {ch} {option.text}", file=file)
            print(end="\n\n", file=file)


async def check_option(
    option_data: OptionData,
    single: bool,
    message: Message,
    state: FSMContext,
    session: AsyncSession,
):
    data = await state.get_data()
    if question := await find_question(
        option_data.quiz_id,
        option_data.q_n,
        session,
    ):
        answers: dict[str, list[int]] = data.get("answers", {})
        answer = answers.setdefault(str(option_data.q_n), [])
        if option_data.option_id in answer:
            answer.remove(option_data.option_id)
        else:
            answer.append(option_data.option_id)
        await show_question(
            question,
            answer,
            edit=True,
            single=single,
            message=message,
        )
        await state.update_data(answers=answers)


def fmt_result(result: QuizResult) -> str:
    answers: dict[str, set[int]] = {}
    for a in result.answers:
        answer = answers.setdefault(str(a.option.question.n), set())
        answer.add(a.option_id)

    lines = []
    correct_count = 0
    for q in result.quiz.questions:
        tmp = [fmt_question(q)]
        options = {o.id: o for o in sorted(q.options, key=lambda o: o.n)}
        answer = set(answers.get(str(q.n), []))
        correct_answer = True
        for option_id, option in options.items():
            if option_id in answer:
                if option.correct:
                    ch = "✅"
                else:
                    ch = "❌"
                    correct_answer = False
            else:
                if option.correct:
                    ch = "☑"
                    correct_answer = False
                else:
                    ch = "⚪"
            tmp.append(f"{ch} {html.code(option.text)}")

        if correct_answer:
            correct_count += 1
        else:
            lines.extend(tmp)
            lines.append("")

    total = len(result.quiz.questions)
    lines.insert(
        0,
        "<b>"
        f"Quiz: {result.quiz.name}\n"
        f"Result: {correct_count} / {total}\n"
        f"DateTime: {result.created_at}"
        "</b>\n",
    )
    return "\n".join(lines)


async def show_question_in_group(
    quiz_id: int,
    q_n: int,
    session: AsyncSession,
    message: Message,
    bot: Bot,
):
    if (q := await find_question(quiz_id, q_n, session)) is None:
        await message.answer("Question not found!")
        return

    logger.debug(f"{q.id=} {q.n=} {q.text=}")

    correct_options = {opt.n for opt in q.options if opt.correct}
    multiple_answers = len(correct_options) != 1
    option_texts = [opt.text for opt in sorted(q.options, key=lambda o: o.n)]
    link = await create_start_link(bot, payload=f"{quiz_id}_{q.n}")
    link_line = html.link("Go to answer", link)

    if q.code or multiple_answers:
        logger.debug("TEXT MESSAGE")
        lines = [fmt_question(q, quiz_id)]
        lines.extend("⚪ " + html.code(text) for text in option_texts)
        lines.append(link_line)
        await message.answer(
            "\n".join(lines),
            link_preview_options=LinkPreviewOptions(is_disabled=True),
            parse_mode=ParseMode.HTML,
        )
    else:
        logger.debug("PollType.QUIZ")
        correct_option_id = next(iter(correct_options)) - 1
        await message.answer_poll(
            question=f"{quiz_id}.{q.n}. {q.text}",
            options=option_texts,
            is_anonymous=False,
            type=PollType.QUIZ,
            allows_multiple_answers=multiple_answers,
            correct_option_id=correct_option_id,
            disable_notification=True,
            # explanation=q.explanation,
            # explanation_parse_mode=ParseMode.HTML,
        )


async def show_files(
    message: Message,
    state: FSMContext,
    context: BotContext,
    session: AsyncSession,
    edit: bool,
):
    files: dict[str, tuple] = {}
    count = 0
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
            count += 1
            if count > FILE_COUNT:
                break

    await state.set_data(dict(files=files))
    await files_page.show(message, 0, edit, files=files)