#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import requests
import redis
from functools import wraps
from typing import Callable

CACHE = redis.Redis()


def cache_decorator(func: Callable) -> Callable:
    """Decorator to cache the result of a function with expiration time."""

    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function to add caching and counting functionality."""
        count_key = f"request_count:{url}"
        result_key = f"response_result:{url}"

        CACHE.incr(count_key)
        result = CACHE.get(result_key)

        if result:
            return result.decode('utf-8')

        result = func(url)

        CACHE.set(count_key, 0)
        CACHE.setex(result_key, 10, result)

        return result

    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """Get the response content for a given URL."""
    return requests.get(url).text
