import time
from collections import defaultdict, deque
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: float = 60.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._requests = defaultdict(deque)
        self._lock = Lock()

    def allow(self, user_id: str) -> bool:
        now = time.monotonic()
        with self._lock:
            q = self._requests[user_id]
            while q and now - q[0] > self.window_seconds:
                q.popleft()
            if len(q) < self.max_requests:
                q.append(now)
                return True
            return False

# Usage:
# limiter = RateLimiter(max_requests=60, window_seconds=60)
# if limiter.allow(user_id):
#     process_request()
# else:
#     reject_request()  # e.g., raise 429 Too Many Requests