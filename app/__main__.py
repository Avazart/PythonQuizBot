import asyncio
import contextlib
import logging
import sys
from pathlib import Path

import colorama
from aiogram import Bot, Dispatcher, F, Router
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram.types import (
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
)
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm.exc import LoaderStrategyException

from .bot.dumpable_memory_storage import DumpableMemoryStorage
from .bot.filters.filers import BotAdminFilter
from .bot.handlers import bot_admins, group_users, users_in_private
from .bot.middlewares.database_middlewares import DatabaseMiddleware
from .bot.pages import PageId, PageItemData
from .bot.scenes.quiz_scene import QuizScene
from .bot.types import BotContext
from .database.base import Base
from .database.utils.users import get_user_by_id
from .settings import GROUP_COMMANDS, PRIVATE_COMMANDS, Settings
from .utils.logging_utils import (
    decorate_router_handlers,
    decorate_scene_handlers,
    init_logging,
)

logger = logging.getLogger(Path(__file__).parent.name)


async def create_db_if_not_exists(session_maker, engine):
    async with session_maker.begin() as session:
        try:
            # check users table
            await get_user_by_id(1, session)
        except (OperationalError, LoaderStrategyException):
            # create all tables
            async with engine.begin() as connection:
                await connection.run_sync(Base.metadata.create_all)


async def on_startup(bot: Bot):
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(
        PRIVATE_COMMANDS,
        BotCommandScopeAllPrivateChats(),
    )
    await bot.set_my_commands(
        GROUP_COMMANDS,
        BotCommandScopeAllGroupChats(),
    )
    logger.info("Bot started.")


async def main():
    colorama.init()
    load_dotenv(dotenv_path=sys.argv[1] if len(sys.argv) == 2 else None)
    settings = Settings()
    init_logging(settings.log_dir, settings.log_config)

    logger.info("Create database engine ...")
    engine = create_async_engine(
        settings.database_url.get_secret_value(),
        echo=False,
    )
    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    await create_db_if_not_exists(session_maker, engine)

    logger.info("Create bot instance ...")
    bot = Bot(token=settings.bot_token.get_secret_value())
    with DumpableMemoryStorage("app_data/storage.pickle") as storage:
        dp = Dispatcher(
            storage=storage,
            events_isolation=SimpleEventIsolation(),
        )

        database_middleware = DatabaseMiddleware()
        database_middleware.setup(dp)

        dp.startup.register(on_startup)
        bot_admin_filter = BotAdminFilter()
        bot_admins.router.callback_query.filter(bot_admin_filter)
        bot_admins.router.message.filter(bot_admin_filter)

        quiz_router = Router()
        quiz_router.callback_query.register(
            QuizScene.as_handler(),
            PageItemData.filter(F.id == PageId.SELECT_QUIZZES),
        )

        dp.include_routers(
            users_in_private.router,
            group_users.router,
            bot_admins.router,
            # QuizScene.as_router(),
            quiz_router,
        )

        decorate_router_handlers(dp)
        decorate_scene_handlers(QuizScene)

        scene_registry = SceneRegistry(dp)
        scene_registry.add(QuizScene)

        context = BotContext(settings, session_maker)
        await dp.start_polling(bot, context=context)


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
