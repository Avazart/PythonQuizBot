import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.sql.expression import select

from ..models import Answer, Option, Question, Quiz, QuizResult

logger = logging.getLogger(__name__)


async def get_last_quiz_result(
    user_id: int,
    s: AsyncSession,
) -> QuizResult | None:
    return await s.scalar(
        select(QuizResult)
        .filter(QuizResult.user_id == user_id)
        .order_by(QuizResult.created_at.desc())
        .limit(1)
        .options(
            joinedload(QuizResult.answers)
            .joinedload(Answer.option)
            .joinedload(Option.question)
        )
    )


async def find_user_results(
    user_id: int,
    offset: int,
    limit: int,
    s: AsyncSession,
) -> list[QuizResult]:
    r = await s.scalars(
        select(QuizResult)
        .where(QuizResult.user_id == user_id)
        .order_by(QuizResult.created_at.desc())
        .offset(offset)
        .limit(limit)
        .options(joinedload(QuizResult.quiz))
    )
    return r.all()  # type: ignore


async def get_result(
    result_id: int,
    s: AsyncSession,
) -> QuizResult | None:
    return await s.scalar(
        select(QuizResult)
        .where(QuizResult.id == result_id)
        .order_by(QuizResult.created_at)
        .options(
            joinedload(QuizResult.quiz)
            .joinedload(Quiz.questions)
            .joinedload(Question.options),
            selectinload(QuizResult.answers),
        )
    )
