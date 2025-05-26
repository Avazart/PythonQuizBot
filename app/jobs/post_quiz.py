import asyncio
import logging

from aiogram import Bot
from aiogram.exceptions import TelegramRetryAfter

from ..bot.dumpable_memory_storage import DumpableMemoryStorage
from ..database.utils.quizzes import QuizInfo, get_quizzes_info
from ..utils.quiz_utils import show_question_in_group

logger = logging.getLogger(__name__)


def next_pair(
    quiz_n: int,
    question_n: int,
    quizzes: list[QuizInfo],
) -> tuple[int, int]:
    question_n += 1

    if question_n > quizzes[quiz_n].question_count:
        quiz_n += 1
        question_n = 1

    if quiz_n >= len(quizzes):
        quiz_n = 1
        question_n = 1

    return quiz_n, question_n


async def post_quiz_job(
    chat_ids: frozenset[int],
    storage: DumpableMemoryStorage,
    session_maker,
    bot: Bot,
):
    logger.debug("post_quiz")

    async with session_maker() as session:
        if not (quizzes := await get_quizzes_info(0, None, session)):
            logger.error("No quizzes!")
            return

        quiz_n = storage.storage.get("quiz_n", 0)
        q_n = storage.storage.get("question_n", 0)
        logger.debug("Quiz count: %d", len(quizzes))

        quiz_n, q_n = next_pair(quiz_n, q_n, quizzes)

        quiz = quizzes[quiz_n].quiz
        logger.debug("Question: %d(%d).%d", quiz.id, quiz_n, q_n)

        for chat_id in chat_ids:
            for _ in range(3):
                try:
                    await show_question_in_group(
                        chat_id, quiz.id, q_n, session, bot
                    )
                    await asyncio.sleep(0.2)
                    break
                except TelegramRetryAfter as e:
                    await asyncio.sleep(e.retry_after)

        storage.storage["quiz_n"] = quiz_n
        storage.storage["question_n"] = q_n
        storage.dump()
