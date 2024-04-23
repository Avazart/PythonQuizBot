import asyncio
import math
import re
from collections.abc import Iterable, Iterator, Sequence
from itertools import islice

from aiogram.exceptions import TelegramRetryAfter
from aiogram.types import Message

from ..settings import MAX_MESSAGE_LENGHT


def batched_v(iterable: Iterable, n: int) -> Iterator[tuple]:
    # batched_evenly('1234567', 3) --> 147 25 36

    for i in range(n):
        if row := tuple(islice(iterable, i, None, n)):
            yield row
        else:
            return None


def batched_evenly(seq: Sequence, max_batch_size: int) -> Iterator[Sequence]:
    """Batch data evenly with max_batch_size"""

    # batched_evenly('1234567', 3) --> 123 45 67

    total = len(seq)
    batch_count = math.ceil(total / max_batch_size)

    i = 0
    while i < total:
        batch_size = math.ceil((total - i) / batch_count)
        batch = seq[i : i + batch_size]
        yield batch
        i += batch_size
        batch_count -= 1


def adjust(seq: Sequence, row_count: int = 9) -> list[list]:
    if len(seq) <= row_count:
        return [[e] for e in seq]
    else:
        return list(map(list, batched_v(seq, row_count)))


async def try_send(message: Message, attempts: int = 10, **kwargs):
    last_exception = None
    for _ in range(attempts):
        try:
            await message.answer(**kwargs)
            await asyncio.sleep(0.2)
            return
        except TelegramRetryAfter as e:
            last_exception = e
            await asyncio.sleep(e.retry_after)
    if last_exception:
        raise last_exception


async def send_parts(
    message: Message,
    parts: list[str],
    sep: str = "\n",
    **kwargs,
):
    assert parts

    message_parts = [parts[0]]
    lenght = len(parts[0])

    for part in parts[1:]:
        if lenght + len(sep) + len(part) < MAX_MESSAGE_LENGHT:
            message_parts.append(part)
            lenght += len(sep) + len(part)
        else:
            await try_send(
                message=message,
                text=sep.join(message_parts),
                **kwargs,
            )
            message_parts = [part]
            lenght = len(part)

    if message_parts:
        await try_send(
            message=message,
            text=sep.join(message_parts),
            **kwargs,
        )


def text_wrap(text: str, width: int, sep: str = " ") -> list[str]:
    parts = re.split(r"[ \t]+", text)
    lines = []
    line_parts = [parts[0]] if parts else []
    length = len(parts[0])
    for part in parts[1:]:
        if length + len(part) + len(sep) < width:
            line_parts.append(part)
            length += len(part) + len(sep)
        else:
            lines.append(sep.join(line_parts))
            line_parts = [part]
            length = len(part)
    if line_parts:
        lines.append(sep.join(line_parts))
    return lines
