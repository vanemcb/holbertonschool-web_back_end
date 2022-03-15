#!/usr/bin/env python3
"""Module Cache class
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a single method Callable argument
    and returns a Callable.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Function that increments the count for that key every time the
        method is called and returns the value returned by the original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Cache class
    """
    def __init__(self):
        """Constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that generates a random key, stores the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """Convert the data back to the desired format
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Method that automatically parametrize Cache.get to string
        """
        data = self._redis.get(key)
        return str(data.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Method that automatically parametrize Cache.get to int
        """
        data = self._redis.get(key)
        return int(data.decode("utf-8"))
