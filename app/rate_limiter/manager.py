from .factory import RateLimiterFactory

class RateLimiterManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Example initialization with a fixed window rate limiter
            cls._instance.rate_limiter = RateLimiterFactory.create_rate_limiter('fixed', 100, 60000)
        return cls._instance

    def allow_request(self, client_id: str) -> bool:
        return self.rate_limiter.allow_request(client_id)
    