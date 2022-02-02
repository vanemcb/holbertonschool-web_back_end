#!/usr/bin/env python3
""" Coroutine called async_generator """
from array import array
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Coroutine that collects 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers. """
    array_numbers = [i async for i in async_generator()]
    return array_numbers