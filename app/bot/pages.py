import enum
import itertools
import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from ..database.utils.quizzes import QuizInfo, get_quizzes_info
from ..database.utils.users import UserInfo, get_users_info
from ..settings import FILE_COUNT, QUIZ_COUNT, USER_COUNT, Icon
from ..utils.aux_utils import adjust

logger = logging.getLogger(__name__)


class PageId(enum.IntEnum):
    FILES = enum.auto()
    MANAGE_QUIZZES = enum.auto()
    SELECT_QUIZZES = enum.auto()
    USERS = enum.auto()


class PageItemData(CallbackData, prefix="page_item"):
    id: PageId
    item_id: int


class PageShowData(CallbackData, prefix="page_show"):
    id: PageId
    offset: int


class PageCloseData(CallbackData, prefix="page_close"):
    id: PageId


@dataclass(frozen=True)
class Page:
    id: PageId
    text: str
    limit: int

    items_getter: Callable[[int, int, Any], Awaitable[list]]
    item_text_getter: Callable[[Any], str]
    item_id_getter: Callable[[Any], int]

    def _keyboard(
        self,
        items: list,
        prev_offset: int | None,
        next_offset: int | None,
    ) -> InlineKeyboardMarkup:
        buttons = [
            InlineKeyboardButton(
                text=self.item_text_getter(item),
                callback_data=PageItemData(
                    id=self.id,
                    item_id=self.item_id_getter(item),
                ).pack(),
            )
            for item in items
        ]
        keyboard = adjust(buttons)
        nav_buttons = [
            InlineKeyboardButton(
                text=f"{Icon.CLOSE} Close",
                callback_data=PageCloseData(id=self.id).pack(),
            )
        ]
        if prev_offset is not None:
            prev_button = InlineKeyboardButton(
                text=f"{Icon.LEFT} Preview",
                callback_data=PageShowData(
                    id=self.id,
                    offset=prev_offset,
                ).pack(),
            )
            nav_buttons.append(prev_button)
        if next_offset is not None:
            next_button = InlineKeyboardButton(
                text=f"Next {Icon.RIGHT}",
                callback_data=PageShowData(
                    id=self.id,
                    offset=next_offset,
                ).pack(),
            )
            nav_buttons.append(next_button)
        keyboard.append(nav_buttons)
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    async def show(
        self,
        message: Message,
        offset: int,
        edit: bool = False,
        **kwargs,
    ):
        items = await self.items_getter(offset, self.limit + 1, **kwargs)
        prev_offset = max(0, offset - self.limit) if offset > 0 else None
        next_offset = offset + self.limit if len(items) > self.limit else None
        markup = self._keyboard(items[: self.limit], prev_offset, next_offset)
        method = "edit_text" if edit else "answer"
        await getattr(message, method)(self.text, reply_markup=markup)


# Quizzes


async def _get_quizzes(offset: int, limit: int, session) -> list:
    return await get_quizzes_info(offset, limit, session)


def _get_quiz_text(q: QuizInfo) -> str:
    return f"{q.quiz.id}. {q.quiz.name} ({q.question_count})"


# Users


async def _get_users(offset: int, limit: int, session) -> list:
    return await get_users_info(offset, limit, session)


def _get_user_text(u: UserInfo) -> str:
    return f"{u.user.username or u.user.full_name} ({u.result_count})"


# Files


async def _get_files(offset: int, limit: int, files: dict) -> list:
    return list(itertools.islice(files.items(), offset, offset + limit))


def _get_file_text(file: tuple) -> str:
    name, file_name, _, exist = file[1]
    ch = Icon.UPDATE if exist else Icon.UP
    return f"{ch} {file_name}"


manage_quizzes_page = Page(
    id=PageId.MANAGE_QUIZZES,
    text="Quizzes:",
    limit=QUIZ_COUNT,
    items_getter=_get_quizzes,
    item_text_getter=_get_quiz_text,
    item_id_getter=lambda q: q.quiz.id,
)

select_quizzes_page = Page(
    id=PageId.SELECT_QUIZZES,
    text="Quizzes:",
    limit=QUIZ_COUNT,
    items_getter=_get_quizzes,
    item_text_getter=_get_quiz_text,
    item_id_getter=lambda q: q.quiz.id,
)

users_page = Page(
    id=PageId.USERS,
    text="Users:",
    limit=USER_COUNT,
    items_getter=_get_users,
    item_text_getter=_get_user_text,
    item_id_getter=lambda u: u.user.id,
)

files_page = Page(
    id=PageId.FILES,
    text="Files:",
    limit=FILE_COUNT,
    items_getter=_get_files,
    item_text_getter=_get_file_text,
    item_id_getter=lambda f: int(f[0]),
)
