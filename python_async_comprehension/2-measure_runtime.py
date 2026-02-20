#!/usr/bin/env python3
"""Module that contains measure_runtime coroutine."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure runtime."""
    start = time.time()

    task1 = asyncio.create_task(async_comprehension())
    task2 = asyncio.create_task(async_comprehension())
    task3 = asyncio.create_task(async_comprehension())
    task4 = asyncio.create_task(async_comprehension())

    await asyncio.gather(task1, task2, task3, task4)

    end = time.time()
    return end - start
