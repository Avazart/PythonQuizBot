import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import select

from ..models import SingleAnswer

logger = logging.getLogger(__name__)


async def find_single_answers(
    group_id: int,
    message_id: int,
    user_id: int | None,
    s: AsyncSession,
) -> list[SingleAnswer]:
    if user_id is None:
        stmt = (
            select(SingleAnswer)
            .where(
                (SingleAnswer.group_id == group_id)
                & (SingleAnswer.message_id == message_id)
            )
            .options(
                joinedload(SingleAnswer.option), joinedload(SingleAnswer.user)
            )
            .order_by(SingleAnswer.user_id)
        )
    else:
        stmt = (
            select(SingleAnswer)
            .where(
                (SingleAnswer.group_id == group_id)
                & (SingleAnswer.message_id == message_id)
                & (SingleAnswer.user_id == user_id)
            )
            .options(
                joinedload(SingleAnswer.option), joinedload(SingleAnswer.user)
            )
            .order_by(SingleAnswer.user_id)
        )
    r = await s.scalars(stmt)
    return r.all()  # type: ignore
