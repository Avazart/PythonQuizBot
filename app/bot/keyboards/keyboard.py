import logging

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from ...quiz_parser import Question, Quiz
from ...settings import Icon
from ...utils.aux_utils import adjust
from ..types import (
    Action,
    ApplyData,
    BackData,
    CloseData,
    ExitQuizData,
    MoreResultsData,
    NextQuestionData,
    OptionData,
    QuizData,
    ResultData,
    StopUploadingData,
    UpdateResultsData,
)

logger = logging.getLogger(__name__)


def make_quiz_text(quiz: Quiz, count: int) -> str:
    return f"{quiz.id}. {quiz.name} ({count})"


def _close_button() -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text=f"{Icon.CLOSE} Close",
        callback_data=CloseData().pack(),
    )


def main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [[KeyboardButton(text="Quizzes")]]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def question_keyboard(
    question: Question,
    answer: list[int],
    single: bool,
) -> InlineKeyboardMarkup:
    buttons = []
    for option in sorted(question.options, key=lambda o: o.n):
        checked = option.id in answer
        ch = Icon.CHECKED if checked else Icon.UNCHEKED
        button = InlineKeyboardButton(
            text=f"{ch} {option.text}",
            callback_data=OptionData(
                quiz_id=question.quiz_id,
                q_n=question.n,
                q_id=question.id,
                option_id=option.id,
            ).pack(),
        )
        buttons.append(button)

    keyboard = adjust(buttons)
    if not single:
        exit_button = InlineKeyboardButton(
            text=f"{Icon.CLOSE} Exit",
            callback_data=ExitQuizData().pack(),
        )
        next_button = InlineKeyboardButton(
            text=f"Next {Icon.RIGHT}",
            callback_data=NextQuestionData().pack(),
        )
        keyboard.append([exit_button, next_button])
    else:
        apply_button = InlineKeyboardButton(
            text=f"Apply {Icon.RIGHT}",
            callback_data=ApplyData(
                quiz_id=question.quiz_id,
                q_n=question.n,
            ).pack(),
        )
        keyboard.append([apply_button])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def quiz_tool_keyboard(quiz: Quiz) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(
            text=f"{Icon.DOWN} Download",
            callback_data=QuizData(action=Action.DOWNLOAD, id=quiz.id).pack(),
        ),
        InlineKeyboardButton(
            text=f"{Icon.DELETE} Delete",
            callback_data=QuizData(action=Action.DELETE, id=quiz.id).pack(),
        ),
        InlineKeyboardButton(
            text=f"{Icon.LEFT} Back",
            callback_data=BackData().pack(),
        ),
    ]
    return InlineKeyboardMarkup(inline_keyboard=adjust(buttons))


def result_keyboard(user_id: int, result_id: int, next_offset: int | None):
    buttons = [
        InlineKeyboardButton(
            text="Results",
            callback_data=ResultData(id=result_id).pack(),
        )
    ]
    if next_offset is not None:
        more_button = InlineKeyboardButton(
            text=f"More {Icon.RIGHT}",
            callback_data=MoreResultsData(
                id=user_id,
                offset=next_offset,
            ).pack(),
        )
        buttons.append(more_button)
    return InlineKeyboardMarkup(inline_keyboard=[buttons])


def stop_uploading_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{Icon.CLOSE} Stop files uploading",
                    callback_data=StopUploadingData().pack(),
                ),
            ]
        ]
    )


def update_results_keyboard(message_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            _close_button(),
            InlineKeyboardButton(
                text=f"{Icon.UPDATE} Update",
                callback_data=UpdateResultsData(message_id=message_id).pack(),
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
