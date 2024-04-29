import enum
import itertools
import logging
import os
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .database.models import Option, Question, Quiz

logger = logging.getLogger(__name__)


class QuizParserException(Exception):
    def __init__(self, text, line_n: int | None = None):
        self._line_n = line_n
        super().__init__(text)

    def __str__(self):
        if self._line_n is None:
            return super().__str__()
        else:
            return f"#{self._line_n} {super().__str__()}"


class LineType(enum.StrEnum):
    EMPTY = ""
    COMMENT = "#"
    TEXT = "?"
    CODE = "code"
    CORRECT = "+"
    WRONG = "-"
    EXPLANATION = "!"
    HINT = "*"
    LINK = ">"
    CONTINUE = "/"


PATTERN = re.compile(r"^#\s*([-?+#>!*/])\s(.*)$")


@dataclass
class Line:
    type: LineType
    text: str
    n: int


class QuizParser:
    def __init__(self, source: Iterable[str]):
        self._cursor: Line | None = None
        self._line_it = self._read_lines(source)
        self._qustion_n = 1

    def _read_lines(self, source: Iterable[str]) -> Iterator[Line]:
        for n, text in enumerate(source, 1):
            if text := text.rstrip():
                if m := PATTERN.match(text):
                    lt, text = m.group(1), m.group(2)
                    self._cursor = Line(LineType(lt), text, n)
                else:
                    self._cursor = Line(LineType.CODE, text, n)
            else:
                self._cursor = Line(LineType.EMPTY, "", n)

            yield self._cursor
        self._cursor = None

    def __iter__(self):
        return self

    def __next__(self) -> Question:
        q_line_n = self._cursor.n if self._cursor else 1
        text = self._read_question_text()
        code = self._read_code()
        options = self._read_options()
        explanation = self._read_explanation()
        hint = self._read_hint()
        link = self._read_link()
        q = Question(
            text=text,
            code=code,
            explanation=explanation,
            hint=hint,
            link=link,
            options=options,
            n=self._qustion_n,
            line_n=q_line_n,
        )
        self._qustion_n += 1
        return q

    def _read_question_text(self) -> str:
        lines = []
        for line in itertools.chain([self._cursor], self._line_it):
            match line:
                case None | Line(LineType.EMPTY) | Line(LineType.COMMENT):
                    continue
                case Line(LineType.TEXT, text):
                    lines.append(text)
                case Line(LineType.CONTINUE, text):
                    if lines:
                        lines[-1] += " " + text
                    else:
                        break
                case _:
                    return "\n".join(lines)
        raise StopIteration()

    def _read_code(self) -> str | None:
        lines = []
        for line in itertools.chain([self._cursor], self._line_it):
            match line:
                case None | Line(LineType.COMMENT):
                    continue
                case Line(LineType.EMPTY, text) | Line(LineType.CODE, text):
                    lines.append(text)
                case Line(LineType.WRONG) | Line(LineType.CORRECT):
                    return "\n".join(lines).rstrip()
                case _:
                    raise QuizParserException("Wrong file format", line.n)
        return None

    def _read_options(self) -> list[Option]:
        options = []
        n = 1
        for line in itertools.chain([self._cursor], self._line_it):
            match line:
                case None | Line(LineType.EMPTY) | Line(LineType.COMMENT):
                    continue
                case Line(LineType.WRONG, text):
                    options.append(Option(n=n, text=text, correct=False))
                    n += 1
                case Line(LineType.CORRECT, text):
                    options.append(Option(n=n, text=text, correct=True))
                    n += 1
                case (
                    Line(LineType.TEXT)
                    | Line(LineType.EXPLANATION)
                    | Line(LineType.HINT)
                    | Line(LineType.LINK)
                ):
                    break
                case _:
                    raise QuizParserException("Wrong file format ", line.n)

        if not options:
            assert self._cursor
            raise QuizParserException(
                "Wrong qustions options!",
                self._cursor.n,
            )
        return options

    def _read_line_type(self, line_type: LineType) -> str | None:
        lines = []
        for line in itertools.chain([self._cursor], self._line_it):
            match line:
                case None | Line(LineType.EMPTY) | Line(LineType.COMMENT):
                    continue
                case Line(type_, text) if type_ == line_type:
                    lines.append(text)
                case Line(LineType.CONTINUE, text):
                    if lines:
                        lines[-1] += " " + text
                    else:
                        break
                case _:
                    break
        return " ".join(lines) if lines else None

    def _read_explanation(self) -> str | None:
        return self._read_line_type(LineType.EXPLANATION)

    def _read_hint(self) -> str | None:
        return self._read_line_type(LineType.HINT)

    def _read_link(self) -> str | None:
        return self._read_line_type(LineType.LINK)


def get_last_modified(file_path: Path) -> datetime:
    return datetime.fromtimestamp(os.path.getmtime(file_path))


def from_file(file_path: Path, source: str, name: str) -> Quiz:
    last_modified = get_last_modified(file_path)
    with file_path.open("r", encoding="utf-8") as file:
        questions = list(QuizParser(file))
        return Quiz(
            source=source,
            name=name,
            last_modified=last_modified,
            questions=questions,
        )


def from_text(text: str, source: str, name: str) -> Quiz:
    questions = list(QuizParser(text.split("\n")))
    return Quiz(
        source=source,
        name=name,
        last_modified=datetime.now(),
        questions=questions,
    )
