import logging
from collections.abc import Awaitable, Callable
from typing import Any, TypeAlias

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject, Update, User

from ...bot.types import BotContext
from ...database.utils.users import get_or_create_user

logger = logging.getLogger(__name__)

Handler: TypeAlias = Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]]


def _get_from_user(event: Update) -> User | None:
    for _, value in vars(event).items():
        if isinstance(value, TelegramObject):
            if from_user := getattr(value, "from_user", None):
                return from_user
    return None


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Handler,
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        context: BotContext = data["context"]
        async with context.session_maker() as session:
            if isinstance(event, Update) and (
                from_user := _get_from_user(event)
            ):
                if not (user := context.users_cache.get(from_user.id)):
                    user = await get_or_create_user(
                        from_user.id,
                        from_user.username,
                        from_user.first_name,
                        from_user.last_name,
                        from_user.language_code,
                        session,
                    )
                    await session.commit()
                    context.users_cache[from_user.id] = user
                data["user"] = user

            data["session"] = session
            return await handler(event, data)

    def setup(self, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)
