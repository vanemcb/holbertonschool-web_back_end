#!/usr/bin/env python3
""" Asynchronous coroutine wait_random"""

import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function that takes an integer argument and
    waits for a random delay and eventually returns it"""
    delay = await random.randrange(0, max_delay)
    return delay
