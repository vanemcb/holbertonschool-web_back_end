#!/usr/bin/env python3
""" Coroutine called measure_runtime """
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
from time import perf_counter


async def measure_runtime() -> float:
    """ Function that measure the total runtime """
    t1 = perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    t2 = perf_counter()
    return t2 - t1
