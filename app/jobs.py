import contextlib
import logging

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

logger = logging.getLogger(__name__)


async def delete_results_message_job(chat_id: int, message_id: int, bot: Bot):
    with contextlib.suppress(TelegramBadRequest):
        await bot.delete_message(chat_id, message_id)
