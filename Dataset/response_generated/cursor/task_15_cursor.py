import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_api_call(fn: Callable[[], T], *, max_attempts: int = 3, delay: float = 1.0) -> T:
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception:
            if attempt == max_attempts - 1:
                raise
            time.sleep(delay)