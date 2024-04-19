import logging
from collections.abc import Awaitable, Callable
from datetime import datetime, timedelta
from typing import Any, TypeAlias

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject

from ...bot.types import BotContext
from ...settings import GROUP_ANONYMOUS_BOT_ID

logger = logging.getLogger(__name__)

Handler: TypeAlias = Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]]


class GroupMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Handler,
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            user = event.from_user
            chat = event.chat
        elif isinstance(event, CallbackQuery):
            user = event.from_user
            chat = event.message.chat
        else:
            return

        if user:
            context: BotContext = data["context"]
            if (
                user.id in context.settings.bot_admin_ids
                or user.id == GROUP_ANONYMOUS_BOT_ID
            ):
                return await handler(event, data)

            last_activity_time = context.activity_time_cache.get(chat.id)

            if (last_activity_time is None) or (
                datetime.now() - last_activity_time > timedelta(minutes=1)
            ):
                context.activity_time_cache[chat.id] = datetime.now()
                return await handler(event, data)
