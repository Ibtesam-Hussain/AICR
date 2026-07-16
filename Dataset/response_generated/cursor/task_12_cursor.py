import time
from collections import defaultdict
from threading import Lock
from typing import Callable


def create_rate_limiter(max_requests: int, per_seconds: int = 60) -> Callable[[str], bool]:
    """Return a per-user rate limiter: max_requests allowed per window."""
    timestamps: dict[str, list[float]] = defaultdict(list)
    lock = Lock()

    def allow(user_id: str) -> bool:
        now = time.monotonic()
        cutoff = now - per_seconds

        with lock:
            recent = [t for t in timestamps[user_id] if t > cutoff]
            if len(recent) >= max_requests:
                timestamps[user_id] = recent
                return False
            recent.append(now)
            timestamps[user_id] = recent
            return True

    return allow