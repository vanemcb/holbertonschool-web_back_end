#!/usr/bin/env python3
""" Coroutine called async_generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Coroutine that loops 10 times, each
    time asynchronously wait 1 second """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
