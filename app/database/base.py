from datetime import datetime

from sqlalchemy import TIMESTAMP, BigInteger, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ..settings import USE_SQLITE


class SLBigInteger(BigInteger):
    pass


if not USE_SQLITE:

    class Base(DeclarativeBase):
        __abstract__ = True

else:
    # https://docs-sqlalchemy.readthedocs.io/ko/latest/dialects/sqlite.html

    from sqlalchemy import event
    from sqlalchemy.engine import Engine
    from sqlalchemy.ext.compiler import compiles

    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, _):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    @compiles(SLBigInteger, "sqlite")
    def bi_c(element, compiler, **kw):
        return "INTEGER"

    class Base(DeclarativeBase):  # type: ignore
        __abstract__ = True
        __table_args__ = {"sqlite_autoincrement": True}


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        server_default=func.now(),
    )
