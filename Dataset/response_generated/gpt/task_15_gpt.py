import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_api_call(
    func: Callable[..., T],
    *args,
    retries: int = 3,
    delay: float = 1.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
    **kwargs,
) -> T:
    """
    Retries a callable up to `retries` times if it raises one of the specified exceptions.
    """
    last_exception = None

    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except exceptions as exc:
            last_exception = exc
            if attempt == retries - 1:
                break
            time.sleep(delay)

    raise last_exception