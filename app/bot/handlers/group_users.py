import logging
import random
import re

from aiogram import Bot, F, Router
from aiogram.enums import ChatType
from aiogram.filters import Command, CommandObject
from aiogram.types import (
    CallbackQuery,
    Chat,
    Message,
    ReplyKeyboardRemove,
)
from sqlalchemy.ext.asyncio import AsyncSession

from ...database.utils.quizzes import get_quizzes_info
from ...utils.quiz_utils import show_question_in_group, show_results
from ..middlewares.group_middlewares import GroupMiddleware
from ..types import BotContext, CloseData, ShowResultsData

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(F.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP)))
router.callback_query.filter(
    F.message.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP))
)
router.message.middleware(GroupMiddleware())
router.callback_query.middleware(GroupMiddleware())


@router.message(Command(commands=["hide"]))
async def hide_command(message: Message):
    await message.answer("-", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=["quiz"]))
async def quiz_command(
    message: Message,
    command: CommandObject,
    session: AsyncSession,
    bot: Bot,
):
    if not (quizzes := await get_quizzes_info(0, None, session)):
        await message.answer("No quizzes!")
        return

    if args := command.args and re.split(r"[ .-]", command.args):
        try:
            quiz_id = int(args[0])
            quiz, count = next(
                ((qz, count) for qz, count in quizzes if qz.id == quiz_id)
            )
            q_n = int(args[1]) if len(args) >= 2 else random.randint(1, count)
        except (ValueError, TypeError):
            await message.answer("Wrong arguments!")
            return
        except StopIteration:
            await message.answer("Quiz not found!")
            return
    else:
        quiz, count = random.choice(quizzes)
        q_n = random.randint(1, count)

    logger.debug(f"{quiz.id=} {q_n=}")
    await show_question_in_group(quiz.id, q_n, session, message, bot)


@router.message(
    Command(commands=["results"]),
    F.reply_to_message.as_("reply_to_message"),
    F.chat.as_("chat"),
)
async def results_command(
    _: Message,
    reply_to_message: Message,
    chat: Chat,
    session: AsyncSession,
    context: BotContext,
):
    await show_results(
        chat.id,
        reply_to_message.message_id,
        False,
        reply_to_message,
        context.result_messages,
        session,
    )


@router.callback_query(
    ShowResultsData.filter(),
    F.message.as_("message"),
    F.message.chat.as_("chat"),
)
async def show_or_update_results(
    _: CallbackQuery,
    message: Message,
    chat: Chat,
    callback_data: ShowResultsData,
    session: AsyncSession,
    context: BotContext,
):
    await show_results(
        chat.id,
        callback_data.message_id,
        callback_data.edit,
        message,
        context.result_messages,
        session,
    )


@router.callback_query(CloseData.filter(), F.message.as_("message"))
async def handle_close(_: CallbackQuery, message: Message):
    await message.delete()
