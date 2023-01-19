import uuid
import redis
from typing import Union


class Cache:
    """Cache class representation"""

    def __init__(self) -> None:
        """Initialize redis instance"""
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data arg, generates random key, store data in redis with random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
