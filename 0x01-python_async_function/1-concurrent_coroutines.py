#!/usr/bin/env python3
"""
python file on tasks about asyncio module
"""
import asyncio
from main import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    wait_n function returns a list of awaited
    coroutines
    """
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    for i in range(len(delays)):
        for j in range(len(delays) - 1):
            if delays[j] > delays[j + 1]:
                delays[j + 1] = delays[j]

    return delays
