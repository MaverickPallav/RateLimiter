from .fixed_window import FixedWindowRateLimiter
from .sliding_window import SlidingWindowRateLimiter
from .base import RateLimiter

class RateLimiterFactory:
    @staticmethod
    def create_rate_limiter(type: str, max_requests: int, window_size_in_millis: int) -> 'RateLimiter':
        if type.lower() == 'fixed':
            return FixedWindowRateLimiter(max_requests, window_size_in_millis)
        elif type.lower() == 'sliding':
            return SlidingWindowRateLimiter(max_requests, window_size_in_millis)
        else:
            raise ValueError("Unknown rate limiter type")

