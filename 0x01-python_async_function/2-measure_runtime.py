#!/usr/bin/env python3
""" Function measure_time """
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function that measures the total execution time for wait_n"""
    counter = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = perf_counter() - counter
    return result
