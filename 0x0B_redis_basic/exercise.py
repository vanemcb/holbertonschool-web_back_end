#!/usr/bin/env python3
"""Module Cache class
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class
    """
    def __init__(self):
        """Constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that generates a random key, stores the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
