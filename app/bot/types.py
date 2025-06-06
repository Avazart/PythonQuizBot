import enum
from dataclasses import dataclass, field

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import State, StatesGroup
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from cachetools import LRUCache
from sqlalchemy.ext.asyncio import async_sessionmaker

from ..settings import CACHE_SIZE, Settings
from .dumpable_memory_storage import DumpableMemoryStorage


@dataclass
class BotContext:
    settings: Settings
    session_maker: async_sessionmaker
    scheduler: AsyncIOScheduler
    storage: DumpableMemoryStorage

    users_cache: LRUCache = field(
        default_factory=lambda: LRUCache(maxsize=CACHE_SIZE),
    )
    activity_time_cache: LRUCache = field(
        default_factory=lambda: LRUCache(maxsize=CACHE_SIZE),
    )
    result_messages: LRUCache = field(
        default_factory=lambda: LRUCache(maxsize=CACHE_SIZE),
    )


class Form(StatesGroup):
    QUIZ = State()
    SINGLE_QUESTION = State()
    UPLOAD = State()
    RENAME_QUIZ = State()


# CallbackData


class LocaleData(CallbackData, prefix="locale"):
    locale: str


@enum.unique
class Action(enum.StrEnum):
    DELETE = enum.auto()
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


class StopUploadingData(CallbackData, prefix="finish"):
    pass


class FileData(CallbackData, prefix="file"):
    file_id: int
    quiz_id: int | None


class CloseData(CallbackData, prefix="close"):
    pass


class ShowResultsData(CallbackData, prefix="show_results"):
    message_id: int
    edit: bool
