#!/usr/bin/env python3
"""
task
"""
import asyncio
wait_random_module = __import__('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


def task_wait_random(max_delay: int):
    """
    returns a asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
