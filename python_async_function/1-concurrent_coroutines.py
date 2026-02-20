#!/usr/bin/env python3
"""Module that defines a function to run multiple coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for finished in asyncio.as_completed(tasks):
        delay = await finished
        delays.append(delay)

    return delays
