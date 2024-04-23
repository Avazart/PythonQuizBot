import logging
from datetime import datetime, timedelta

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

from ...bot.types import BotContext

logger = logging.getLogger(__name__)


class BotAdminFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        mq: Message | CallbackQuery,
        context: BotContext,
    ) -> bool:
        if mq.from_user:
            return mq.from_user.id in context.settings.bot_admin_ids
        return False


class GroupThrottleFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    async def __call__(
        self,
        mq: Message | CallbackQuery,
        context: BotContext,
    ) -> bool:
        if isinstance(mq, Message):
            user = mq.from_user
            chat = mq.chat
        elif isinstance(mq, CallbackQuery):
            user = mq.from_user
            if not mq.message:
                return False
            chat = mq.message.chat
        else:
            return False

        if not user:
            return False

        # if (
        #     user.id in context.settings.bot_admin_ids
        #     or user.id == GROUP_ANONYMOUS_BOT_ID
        # ):
        #     return True

        last_activity_time = context.activity_time_cache.get(chat.id)

        if (last_activity_time is None) or (
            datetime.now() - last_activity_time > timedelta(minutes=1)
        ):
            context.activity_time_cache[chat.id] = datetime.now()
            return True
