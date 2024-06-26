import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import select

from ..models import Option, Question

logger = logging.getLogger(__name__)


async def find_question(
    quiz_id: int,
    n: int,
    s: AsyncSession,
) -> Question | None:
    return await s.scalar(
        select(Question)
        .where((Question.quiz_id == quiz_id) & (Question.n == n))
        .options(joinedload(Question.options))
    )


async def get_options(question_id: int, s: AsyncSession) -> list[Option]:
    r = await s.scalars(
        select(Option).where(Option.question_id == question_id)
    )
    return r.all()  # type: ignore
