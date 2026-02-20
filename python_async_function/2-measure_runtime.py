#!/usr/bin/env python3
"""This module measures the average runtime per coroutine when running wait_n.
It uses time.time to compute the elapsed execution time.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total runtime for wait_n(n, max_delay).
    Return the average time per coroutine as a float.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
