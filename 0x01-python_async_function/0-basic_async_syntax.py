#!/usr/bin/env python3
"""
basics of async
"""

import asyncio
import random
"""
file about the wait_random function
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    a function that uses random method
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
