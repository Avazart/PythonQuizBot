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
    action: str | None = None
    parent_id: int | None = None


class PageShowData(CallbackData, prefix="page_show"):
    id: PageId
    offset: int
    action: str | None = None
    parent_id: int | None = None


class PageCloseData(CallbackData, prefix="page_close"):
    id: PageId
    action: str | None = None
    parent_id: int | None = None


@dataclass
class Page:
    id: PageId
    text: str
    limit: int

    items_getter: Callable[[int, int, Any], Awaitable[list]]
    item_text_getter: Callable[[Any], str]
    item_id_getter: Callable[[Any], int]

    parent_id: int | None = None

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
                    parent_id=self.parent_id,
                ).pack(),
            )
            for item in items
        ]
        keyboard = adjust(buttons)
        nav_buttons = [
            InlineKeyboardButton(
                text=f"{Icon.CLOSE} Close",
                callback_data=PageCloseData(
                    id=self.id,
                    parent_id=self.parent_id,
                ).pack(),
            )
        ]
        if prev_offset is not None:
            prev_button = InlineKeyboardButton(
                text=f"{Icon.LEFT} Preview",
                callback_data=PageShowData(
                    id=self.id,
                    offset=prev_offset,
                    parent_id=self.parent_id,
                ).pack(),
            )
            nav_buttons.append(prev_button)
        if next_offset is not None:
            next_button = InlineKeyboardButton(
                text=f"Next {Icon.RIGHT}",
                callback_data=PageShowData(
                    id=self.id,
                    offset=next_offset,
                    parent_id=self.parent_id,
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


async def get_quizzes(offset: int, limit: int, session):
    return await get_quizzes_info(offset, limit, session)


def get_quiz_text(q: QuizInfo):
    return f"{q.quiz.id}. {q.quiz.name} ({q.question_count})"


# Users


async def get_users(offset: int, limit: int, session):
    return await get_users_info(offset, limit, session)


def get_user_text(u: UserInfo):
    return f"{u.user.username or u.user.full_name} ({u.result_count})"


# Files


async def get_files(offset: int, limit: int, files: dict):
    return list(itertools.islice(files.items(), offset, offset + limit))


def get_file_text(f: tuple):
    name, file_name, _, exist = f[1]
    ch = Icon.UPDATE if exist else Icon.UP
    return f"{ch} {file_name}"


manage_quizzes_page = Page(
    id=PageId.MANAGE_QUIZZES,
    text="Quizzes:",
    limit=QUIZ_COUNT,
    items_getter=get_quizzes,
    item_text_getter=get_quiz_text,
    item_id_getter=lambda q: q.quiz.id,
    parent_id=None,
)

select_quizzes_page = Page(
    id=PageId.SELECT_QUIZZES,
    text="Quizzes:",
    limit=QUIZ_COUNT,
    items_getter=get_quizzes,
    item_text_getter=get_quiz_text,
    item_id_getter=lambda q: q.quiz.id,
    parent_id=None,
)

users_page = Page(
    id=PageId.USERS,
    text="Users:",
    limit=USER_COUNT,
    items_getter=get_users,
    item_text_getter=get_user_text,
    item_id_getter=lambda u: u.user.id,
    parent_id=None,
)

files_page = Page(
    id=PageId.FILES,
    text="Files:",
    limit=FILE_COUNT,
    items_getter=get_files,
    item_text_getter=get_file_text,
    item_id_getter=lambda f: int(f[0]),
    parent_id=None,
)
