#!/usr/bin/env python3
"""
Async generator module.

This module defines an asynchronous generator named async_generator.
It yields ten random floating-point numbers between 0 and 10.
Each value is produced after awaiting a one-second asynchronous delay.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield ten random floating-point numbers between 0 and 10.

    The generator waits one second before yielding each value.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
