#!/usr/bin/env python3
"""Module that contains measure_runtime coroutine."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure runtime."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.time() - start
