#!/usr/bin/env python3
"""This module defines an asynchronous coroutine that waits for a random delay.
The delay is a random float between 0 and max_delay seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait asynchronously for a random delay between 0 and max_delay seconds.
    Return the delay as a float.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
