import math
from collections.abc import Iterable, Iterator, Sequence
from itertools import islice


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
