import time
import logging

logger = logging.getLogger(__name__)

def retry_api_call(func, *args, max_retries=3, delay=1, backoff=2, **kwargs):
    """
    Retries a failing API call up to `max_retries` times with exponential backoff.

    Args:
        func: The function to call (e.g., a requests.get or API client method).
        *args: Positional arguments to pass to func.
        max_retries: Maximum number of attempts before giving up.
        delay: Initial delay (in seconds) between retries.
        backoff: Multiplier applied to delay after each failure.
        **kwargs: Keyword arguments to pass to func.

    Returns:
        The result of func(*args, **kwargs) if successful.

    Raises:
        The last exception raised by func if all retries fail.
    """
    current_delay = delay
    last_exception = None

    for attempt in range(1, max_retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            logger.warning(
                "Attempt %d/%d failed: %s", attempt, max_retries, e
            )
            if attempt < max_retries:
                time.sleep(current_delay)
                current_delay *= backoff

    logger.error("All %d attempts failed.", max_retries)
    raise last_exception