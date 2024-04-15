import logging

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
