from datetime import datetime

from sqlalchemy import (
    DATETIME,
    Boolean,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)

from .base import Base, SLBigInteger, TimeStampMixin


class User(MappedAsDataclass, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(SLBigInteger, primary_key=True)

    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str | None] = mapped_column(
        nullable=True, server_default=None, default=None
    )
    username: Mapped[str | None] = mapped_column(
        nullable=True, server_default=None, default=None
    )
    locale: Mapped[str | None] = mapped_column(
        nullable=True, server_default=None, default=None
    )

    @property
    def full_name(self) -> str:
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name


class Quiz(Base, TimeStampMixin):
    __tablename__ = "quizzes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    source: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    last_modified: Mapped[datetime] = mapped_column(DATETIME)
    active: Mapped[bool] = mapped_column(Boolean, server_default="true")

    questions: Mapped[list["Question"]] = relationship(
        "Question", back_populates="quiz"
    )


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    n: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String)
    code: Mapped[str | None] = mapped_column(String, nullable=True)
    link: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        server_default=None,
    )
    hint: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        server_default=None,
    )
    explanation: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        server_default=None,
    )

    line_n: Mapped[int | None] = mapped_column(
        Integer, nullable=True, server_default=None
    )

    quiz_id = mapped_column(
        ForeignKey(Quiz.id, ondelete="CASCADE", onupdate="CASCADE")
    )

    quiz: Mapped[Quiz] = relationship(Quiz, back_populates="questions")
    options: Mapped[list["Option"]] = relationship(
        "Option", back_populates="question"
    )


class Option(Base):
    __tablename__ = "options"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    n: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(String)
    correct: Mapped[bool] = mapped_column(Boolean)
    question_id = mapped_column(
        ForeignKey(Question.id, ondelete="CASCADE", onupdate="CASCADE")
    )

    question: Mapped[Question] = relationship(
        "Question", back_populates="options"
    )


class QuizResult(Base, TimeStampMixin):
    __tablename__ = "quiz_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id = mapped_column(
        ForeignKey(User.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    quiz_id = mapped_column(
        ForeignKey(Quiz.id, ondelete="CASCADE", onupdate="CASCADE")
    )

    user: Mapped[User] = relationship(User)
    quiz: Mapped[Quiz] = relationship(Quiz)
    answers: Mapped[list["Answer"]] = relationship(
        "Answer", back_populates="result"
    )


class Answer(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    option_id: Mapped[int] = mapped_column(
        ForeignKey(Option.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    result_id = mapped_column(
        ForeignKey(QuizResult.id, ondelete="CASCADE", onupdate="CASCADE")
    )

    option: Mapped[Option] = relationship(Option)
    result: Mapped[QuizResult] = relationship(
        QuizResult, back_populates="answers"
    )
