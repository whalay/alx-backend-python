#!/usr/bin/env python3
"""
    Concurrent programs that measures the total execution
    time for wait_n(n, max_delay)
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ intricately and simply measures  time function """

    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - s
    return end / n
