#!/usr/bin/env python3
"""This module defines an asynchronous generator that yields
ten random floating-point numbers between 0 and 10.
Each value is produced after awaiting a one-second delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random floats between 0 and 10, waiting 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
