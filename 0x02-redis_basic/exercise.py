#!/usr/bin/env python3
"""Writing, Reading, Incrementing values to Redis"""
import uuid
import redis
from typing import Optional, Callable, Union


class Cache:
    """Cache class representation"""

    def __init__(self) -> None:
        """Initialize redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data arg, generates random key,
        store data in redis with random key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn:  Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """takes key and convert data back to desired format"""
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, result: bytes) -> str:
        """convert result to string"""
        return str(result, 'UTF-8')

    def get_int(self, result: bytes) -> int:
        """convert result to int"""
        return int.from_bytes(result, "big")
