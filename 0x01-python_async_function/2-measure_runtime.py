#!/usr/bin/env python3
"""
task 
"""
import asyncio
import time
wait_n_module = __import__('1-concurrent_coroutines')
wait_n = wait_n_module.wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures time takesn to await for coroutines
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
