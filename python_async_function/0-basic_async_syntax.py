#!/usr/bin/env python3
"""This module defines an asynchronous coroutine that waits for a random delay between zero and the provided maximum delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random float between 0 and max_delay after waiting asynchronously."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
