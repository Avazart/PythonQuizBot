import asyncio
import contextlib
import itertools
import logging
import re
from collections.abc import Container
from datetime import datetime
from pathlib import Path

from aiogram import Bot, html
from aiogram.enums import ParseMode, PollType
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import LinkPreviewOptions, Message
from aiogram.utils.deep_linking import create_start_link
from cachetools import LRUCache
from sqlalchemy.ext.asyncio import AsyncSession

from ..bot.keyboards.keyboard import (
    goto_answer_keyboard,
    question_keyboard,
    update_results_keyboard,
)
from ..bot.types import OptionData
from ..database.models import Quiz, QuizResult
from ..database.utils.answers import find_single_answers
from ..database.utils.questions import find_question, get_options
from ..database.utils.quizzes import find_quiz, get_quiz_info
from ..quiz_parser import LineType, Question, get_last_modified
from .aux_utils import text_wrap

logger = logging.getLogger(__name__)


def fmt_question(question: Question, quiz_id: int | None = None):
    """
    n.n question_text
    code
    hint
    """
    if quiz_id is None:
        lines = [f"{html.bold(str(question.n))}. {question.text}"]
    else:
        lines = [f"{html.bold(f'{quiz_id}.{question.n}')}. {question.text}"]

    if question.code:
        lines.append(html.pre_language(html.unparse(question.code), "python"))

    if question.hint:
        lines.append(html.spoiler(question.hint))

    if question.link:
        lines.append(
            " ".join(
                html.link(f"[{i}]", link)
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


async def show_results(
    chat_id: int,
    message_id: int,
    edit: bool,
    message: Message,
    result_messages: LRUCache,
    session: AsyncSession,
):
    if not edit and (result := result_messages.pop(message_id, None)):
        with contextlib.suppress(TelegramBadRequest):
            await message.bot.delete_message(result[0], result[1])

    if answers := await find_single_answers(
        chat_id,
        message_id,
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
            lines.append(f"{user.full_name} {ch}")
        if edit:
            lines.append(f"\nLast update: {datetime.now():%H:%M:%S}")

        method = "edit_text" if edit else "reply"
        result_message = await getattr(message, method)(
            text="\n".join(lines),
            parse_mode=ParseMode.HTML,
            reply_markup=update_results_keyboard(message_id),
        )
    else:
        method = "edit_text" if edit else "answer"
        lines = ["No results, yet!"]
        if edit:
            lines.extend(["", f"Last update: {datetime.now():%H:%M:%S}"])

        result_message = await getattr(message, method)(
            text="\n".join(lines),
            reply_markup=update_results_keyboard(message_id),
        )

    if not edit:
        result_messages[message_id] = chat_id, result_message.message_id


def make_quiz_info_text(quiz: Quiz, count: int) -> str:
    return f"{quiz.name} ({count}) [{quiz.last_modified:%H:%M %d.%m.%y}]"


def normalize_file_name(text: str) -> str:
    return re.sub(r'[/\\:*?"<>|]', "_", text)


def parse_file_path(path: Path) -> tuple[int | None, str]:
    if m := re.match(r"^(\d+)\.\s*(.*)", path.stem):
        quiz_id = int(m.group(1))
        name = m.group(2)
    else:
        quiz_id = None
        name = path.stem
    return quiz_id, name


def wrapped(lt: LineType, text: str) -> list[str]:
    result = []
    for line_text in filter(None, text.split("\n")):
        ss = text_wrap(line_text, width=79 - 4)
        if len(ss) > 1:
            first, *other = ss
            first_line = f"# {lt} {first}"
            other_lines = [f"# {LineType.CONTINUE} {text}" for text in other]
            result.append(first_line)
            result.extend(other_lines)
        else:
            result.append(f"# {lt} {ss[0]}")
    return result


def quiz_as_text(quiz: Quiz) -> str:
    lines = []
    for n, question in enumerate(quiz.questions, 1):
        lines.append(f"# # {n:=<75}")
        lines.append("\n")
        lines.extend(wrapped(LineType.TEXT, question.text))
        lines.append("\n")

        if question.code:
            lines.append(f"{question.code}")
            lines.append("\n")

        for option in question.options:
            ch = "+" if option.correct else "-"
            lines.append(f"# {ch} {option.text}")

        if question.explanation:
            lines.append("\n")
            lines.extend(wrapped(LineType.EXPLANATION, question.explanation))

        if question.hint:
            lines.append("\n")
            lines.extend(wrapped(LineType.HINT, question.hint))

        if question.link:
            lines.append("\n")
            lines.extend(wrapped(LineType.LINK, question.link))

        lines.append("\n")
    return "\n".join(lines)


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


def make_answer_text(q: Question, answer: Container[int]) -> tuple[bool, str]:
    """
    question text
    ✅ options
    explanation
    """
    lines = [fmt_question(q)]
    options = {o.id: o for o in sorted(q.options, key=lambda o: o.n)}
    correct = True
    for option_id, option in options.items():
        if option_id in answer:
            if option.correct:
                ch = "✅"
            else:
                ch = "❌"
                correct = False
        else:
            if option.correct:
                ch = "☑"
                correct = False
            else:
                ch = "⚪"
        lines.append(f"{ch} {html.code(html.unparse(option.text))}")

    if q.explanation:
        lines.append("")
        lines.append(q.explanation)

    return correct, "\n".join(lines)


def fmt_result(result: QuizResult) -> list[str]:
    answers: dict[str, set[int]] = {}
    for a in result.answers:
        answer = answers.setdefault(str(a.option.question.n), set())
        answer.add(a.option_id)

    parts = []
    correct_count = 0
    for q in result.quiz.questions:
        answer = answers.get(str(q.n), set())
        correct, text = make_answer_text(q, answer)
        if correct:
            correct_count += 1
        else:
            parts.append(text)

    total = len(result.quiz.questions)
    parts.insert(
        0,
        "<b>"
        f"Quiz: {result.quiz.name}\n"
        f"Result: {correct_count} / {total}\n"
        f"DateTime: {result.created_at}"
        "</b>\n",
    )
    return parts


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

    correct_options = {opt.n for opt in q.options if opt.correct}
    multiple_answers = len(correct_options) != 1
    option_texts = [opt.text for opt in sorted(q.options, key=lambda o: o.n)]
    too_long_for_pool = (len(q.text) >= 300 - 10) or any(
        len(opt) >= 100 - 3 for opt in option_texts
    )
    if q.code or multiple_answers or too_long_for_pool:
        lines = [fmt_question(q, quiz_id)]
        lines.extend(
            "⚪ " + html.code(html.unparse(text)) for text in option_texts
        )
        m = await message.answer(
            "\n".join(lines),
            link_preview_options=LinkPreviewOptions(is_disabled=True),
            parse_mode=ParseMode.HTML,
        )
        params = (quiz_id, q.n, message.chat.id, m.message_id)
        link = await create_start_link(bot, payload="_".join(map(str, params)))
        markup = goto_answer_keyboard(link, m.message_id)
        await asyncio.sleep(0.2)
        await m.edit_reply_markup(reply_markup=markup)
    else:
        correct_option_id = next(iter(correct_options)) - 1
        await message.answer_poll(
            question=f"{quiz_id}.{q.n}. {q.text}",
            options=option_texts,
            is_anonymous=False,
            type=PollType.QUIZ,
            allows_multiple_answers=multiple_answers,
            correct_option_id=correct_option_id,
            disable_notification=True,
            explanation=q.explanation,
            explanation_parse_mode=ParseMode.HTML,
        )


async def scan_files(folder: Path, session: AsyncSession) -> dict[str, tuple]:
    files: dict[str, tuple] = {}
    for i, path in enumerate(folder.glob("*.py")):
        quiz_id, name = parse_file_path(path)
        quiz: Quiz | None = None
        if quiz_id is not None:
            if quiz_info := await get_quiz_info(quiz_id, session):
                quiz, _ = quiz_info
        if not quiz:
            quiz = await find_quiz(name, session)

        if (not quiz) or (get_last_modified(path) > quiz.last_modified):
            files[str(i)] = name, path.name, quiz_id, bool(quiz)
    return files
