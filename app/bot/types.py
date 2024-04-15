import enum
from dataclasses import dataclass, field
from datetime import datetime

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import State, StatesGroup
from cachetools import LRUCache
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..settings import CACHE_SIZE, Settings


@dataclass
class BotContext:
    settings: Settings
    session_maker: async_sessionmaker
    users_cache: LRUCache = field(
        default_factory=lambda: LRUCache(maxsize=CACHE_SIZE),
    )
    last_quiz_time: datetime | None = None


class Form(StatesGroup):
    QUIZ = State()
    SINGLE_QUESTION = State()
    ADD_SOURCE = State()
    RENAME_QUIZ = State()


# CallbackData


class LocaleData(CallbackData, prefix="locale"):
    locale: str


@enum.unique
class Action(enum.StrEnum):
    DELETE = enum.auto()
    UPDATE = enum.auto()
    UPLOAD = enum.auto()
    DOWNLOAD = enum.auto()
    RENAME = enum.auto()


class QuizData(CallbackData, prefix="quiz"):
    action: Action
    id: int
    count: int | None = None


class OptionData(CallbackData, prefix="option"):
    quiz_id: int
    q_n: int
    q_id: int
    option_id: int


class ExitQuizData(CallbackData, prefix="exit"):
    pass


class NextQuestionData(CallbackData, prefix="next"):
    pass


class BackData(CallbackData, prefix="back"):
    pass


class ResultData(CallbackData, prefix="result"):
    id: int


class MoreResultsData(CallbackData, prefix="more"):
    id: int
    offset: int


class ApplyData(CallbackData, prefix="apply"):
    quiz_id: int
    q_n: int


class UserData(CallbackData, prefix="user"):
    id: int


class FinishUploadingData(CallbackData, prefix="finish"):
    pass


class FileData(CallbackData, prefix="file"):
    file_id: int
    quiz_id: int | None


class CloseData(CallbackData, prefix="close"):
    pass
