from typing import Sequence, TypeVar, List

T = TypeVar("T")


def paginate(items: Sequence[T], page: int, page_size: int) -> List[T]:
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1:
        raise ValueError("page_size must be >= 1")

    start = (page - 1) * page_size
    end = start + page_size
    return list(items[start:end])