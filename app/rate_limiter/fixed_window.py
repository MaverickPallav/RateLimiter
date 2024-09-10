import time
from collections import defaultdict
from .base import RateLimiter, AbstractRateLimiter

class FixedWindowRateLimiter(AbstractRateLimiter):
    def __init__(self, max_requests: int, window_size_in_millis: int):
        super().__init__(max_requests, window_size_in_millis)
        self.request_counts = defaultdict(int)
        self.window_start_times = defaultdict(lambda: time.time() * 1000)

    def is_request_allowed(self, client_id: str) -> bool:
        current_time = time.time() * 1000
        window_start_time = self.window_start_times[client_id]

        if current_time - window_start_time >= self.window_size_in_millis:
            self.window_start_times[client_id] = current_time
            self.request_counts[client_id] = 0

        if self.request_counts[client_id] < self.max_requests:
            self.request_counts[client_id] += 1
            return True
        return False
