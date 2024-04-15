import logging
import random
from datetime import datetime, timedelta

from aiogram import Bot, F, Router
from aiogram.enums import ChatType
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from ...database.models import User
from ...database.utils.quizzes import get_quizzes_info
from ...settings import GROUP_ANONYMOUS_BOT_ID, QUIZ_COUNT
from ...utils.quiz_utils import show_question_in_group
from ..types import BotContext

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(F.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP)))
router.callback_query.filter(
    F.message.chat.type.in_((ChatType.GROUP, ChatType.SUPERGROUP))
)


@router.message(Command(commands=["hide"]))
async def hide_command(message: Message):
    await message.answer("-", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands=["quiz"]), F.from_user.as_("from_user"))
async def quiz_command(
    message: Message,
    from_user: User,
    command: CommandObject,
    session: AsyncSession,
    bot: Bot,
    context: BotContext,
):
    if (
        (from_user.id not in context.settings.bot_admin_ids)
        and (from_user.id != GROUP_ANONYMOUS_BOT_ID)
        and context.last_quiz_time
        and (datetime.now() - context.last_quiz_time < timedelta(minutes=5))
    ):
        return

    context.last_quiz_time = datetime.now()

    if not (quizzes := await get_quizzes_info(0, QUIZ_COUNT, session)):
        await message.answer("No quizzes!")
        return

    if args := command.args and command.args.split():
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

    logger.debug(f"{quiz.id=} {quiz.id=} {count=}")

    await show_question_in_group(quiz.id, q_n, session, message, bot)
