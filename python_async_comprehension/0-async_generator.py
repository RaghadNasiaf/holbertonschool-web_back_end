#!/usr/bin/env python3
"""
Module that yields 10 random numbers between 0 and 10.
Each number is generated after waiting 1 second.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop 10 times, wait 1 second each time, and yield a random number
    between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
