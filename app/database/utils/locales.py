import logging

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select

from ..models import User

logger = logging.getLogger(__name__)


async def get_user_locale(user_id: int, s: AsyncSession) -> str | None:
    user = await s.scalar(select(User).filter(User.id == user_id))
    return user.locale if user else None


async def set_user_locale(user_id: int, locale: str, s: AsyncSession) -> None:
    await s.execute(
        update(User).where(User.id == user_id).values(locale=locale)
    )
