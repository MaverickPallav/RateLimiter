import time
from collections import deque, defaultdict
from .base import RateLimiter, AbstractRateLimiter

class SlidingWindowRateLimiter(AbstractRateLimiter):
    def __init__(self, max_requests: int, window_size_in_millis: int):
        super().__init__(max_requests, window_size_in_millis)
        self.request_timestamps = defaultdict(deque)

    def is_request_allowed(self, client_id: str) -> bool:
        current_time = time.time() * 1000
        timestamps = self.request_timestamps[client_id]

        while timestamps and current_time - timestamps[0] > self.window_size_in_millis:
            timestamps.popleft()

        if len(timestamps) < self.max_requests:
            timestamps.append(current_time)
            return True
        return False
