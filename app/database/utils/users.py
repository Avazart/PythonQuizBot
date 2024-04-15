import logging
from typing import NamedTuple

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import functions
from sqlalchemy.sql.expression import select

from ...database import models
from ..models import QuizResult, User

logger = logging.getLogger(__name__)


class UserInfo(NamedTuple):
    user: User
    result_count: int


async def get_user_by_id(user_id: int, s: AsyncSession) -> models.User | None:
    return await s.scalar(
        select(models.User)
        .filter(models.User.id == user_id)
        .options(joinedload(models.User.locale))
    )


async def get_or_create_user(
    user_id: int,
    username: str | None,
    first_name: str,
    last_name: str | None,
    locale: str | None,
    s: AsyncSession,
) -> User:
    result = await s.scalar(
        insert(User)
        .values(
            id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            locale=locale,
        )
        .on_conflict_do_update(
            index_elements=[User.id],
            set_=dict(
                username=username,
                first_name=first_name,
                last_name=last_name,
            ),
        )
        .returning(User)
    )
    return result  # type: ignore


async def get_users(
    offset: int,
    limit: int,
    s: AsyncSession,
) -> list[models.User]:
    r = await s.scalars(select(User).offset(offset).limit(limit))
    return r.all()  # type: ignore


async def get_users_info(
    offset: int,
    limit: int,
    s: AsyncSession,
) -> list[UserInfo]:
    r = await s.execute(
        select(User, functions.count(QuizResult.id))
        .outerjoin(QuizResult, User.id == QuizResult.user_id)
        .group_by(User.id)
        .order_by(functions.count(QuizResult.id).desc())
        .offset(offset)
        .limit(limit)
    )
    return [UserInfo(*r) for r in r.all()]
