import logging
from typing import NamedTuple

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import count

from ..models import Question, Quiz

logger = logging.getLogger(__name__)


class QuizInfo(NamedTuple):
    quiz: Quiz
    question_count: int

    def __bool__(self):
        return self.quiz is not None


async def get_quizzes_info(
    offset: int,
    limit: int,
    s: AsyncSession,
) -> list[QuizInfo]:
    r = await s.execute(
        select(Quiz, count(Question.id))
        .join(Question, Question.quiz_id == Quiz.id)
        .group_by(Quiz.id)
        .order_by(Quiz.id)
        .offset(offset)
        .limit(limit)
    )
    return [QuizInfo(*r) for r in r.all()]


async def get_quiz_info(
    quiz_id: int,
    s: AsyncSession,
    full_info: bool = False,
) -> QuizInfo | None:
    if full_info:
        r1 = await s.scalar(
            select(Quiz)
            .filter(Quiz.id == quiz_id)
            .options(joinedload(Quiz.questions).joinedload(Question.options))
        )
        if not r1:
            return None
        return QuizInfo(r1, len(r1.questions))
    else:
        r2 = await s.execute(
            select(Quiz, count(Question.id))
            .filter(Quiz.id == quiz_id)
            .join(Question, Question.quiz_id == Quiz.id)
            .group_by(Quiz.id)
        )
        if r2 and (info := r2.one_or_none()):
            return QuizInfo(*info)  # type: ignore
        else:
            return None


async def find_quiz(name: str, s: AsyncSession) -> Quiz | None:
    return await s.scalar(select(Quiz).filter(Quiz.name == name))


async def delete_quiz(quiz_id: int, s: AsyncSession) -> None:
    await s.execute(delete(Quiz).filter(Quiz.id == quiz_id))
