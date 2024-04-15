"""create tables

Revision ID: 47f220b49233
Revises:
Create Date: 2024-04-05 19:07:28.322739

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
from app.database.base import SLBigInteger

revision = "47f220b49233"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "quizzes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("last_modified", sa.DATETIME(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "users",
        sa.Column("id", SLBigInteger(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("locale", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("code", sa.String(), nullable=True),
        sa.Column("n", sa.Integer(), nullable=True),
        sa.Column("line_n", sa.Integer(), nullable=True),
        sa.Column("quiz_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["quiz_id"], ["quizzes.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "quiz_results",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", SLBigInteger(), nullable=True),
        sa.Column("quiz_id", sa.Integer(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["quiz_id"], ["quizzes.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "options",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("option_id", sa.Integer(), nullable=False),
        sa.Column("result_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["option_id"],
            ["options.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["result_id"],
            ["quiz_results.id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sqlite_autoincrement=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("answers")
    op.drop_table("options")
    op.drop_table("quiz_results")
    op.drop_table("questions")
    op.drop_table("users")
    op.drop_table("quizzes")
    # ### end Alembic commands ###
