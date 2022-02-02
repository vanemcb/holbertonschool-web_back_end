#!/usr/bin/env python3
""" Asynchronous coroutine wait_n"""
from array import array
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function taht executes wait_random n times"""
    array_delay = []
    for i in range(n):
        delay = asyncio.create_task(wait_random(max_delay))
        array_delay.append(await delay)

    return array_delay
