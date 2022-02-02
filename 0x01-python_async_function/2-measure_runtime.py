#!/usr/bin/env python3
""" Function measure_time """
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Function that measures the total execution time for wait_n"""
    t1 = time()
    asyncio.run(wait_n(n, max_delay))
    t2 = time()

    return t2 - t1
