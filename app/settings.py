import enum
from pathlib import Path
from typing import Final

from aiogram.types import BotCommand
from pydantic import SecretStr
from pydantic_settings import BaseSettings

PRIVATE_COMMANDS: Final[list] = [
    BotCommand(
        command="/start",
        description="Start working with the bot",
    ),
    BotCommand(
        command="/files",
        description="Show list of local files (only for bot admins)",
    ),
    BotCommand(
        command="/upload",
        description="Activate uploading quiz files (only for bot admins)",
    ),
    BotCommand(
        command="/download_all",
        description="Download all quizzes as files (only for bot admins)",
    ),
    BotCommand(
        command="/manage_quizzes",
        description="Allow manage quizzes(only for bot admins)",
    ),
    BotCommand(
        command="/users",
        description="Show list of all users (only for bot admins)",
    ),
]

GROUP_COMMANDS: Final[list] = [
    BotCommand(
        command="/quiz",
        description="Post random question from random quiz to group",
    ),
    BotCommand(
        command="/hide",
        description="Hide reply keyboard",
    ),
]

USE_SQLITE: Final[bool] = True
CACHE_SIZE: Final[int] = 1000
FILE_COUNT: Final[int] = 9
QUIZ_COUNT: Final[int] = 9
USER_COUNT: Final[int] = 9 * 3
RESULT_COUNT: Final[int] = 5
GROUP_ANONYMOUS_BOT_ID: Final[int] = 1087968824  # GroupAnonymousBot
CHANNEL_TELEGRAM_ID: Final[int] = 777000  # Telegram
MAX_MESSAGE_LENGHT: Final[int] = 4096


class Icon(enum.StrEnum):
    UNCHEKED = "🟩"
    CHECKED = "✅"
    CLOSE = "🚫"
    UPDATE = "🔄"
    DELETE = "❌"
    LEFT = "⬅"
    RIGHT = "➡"
    UP = "⬆"
    DOWN = "⬇"


class Settings(BaseSettings):
    bot_token: SecretStr
    notion_token: SecretStr
    bot_admin_ids: frozenset[int]
    database_url: SecretStr

    log_dir: Path
    log_config: Path

    notion_parent_pade_id: str
    quiz_folder: Path = Path("app_data/quizzes/")
