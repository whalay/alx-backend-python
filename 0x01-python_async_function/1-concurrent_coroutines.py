#!/usr/bin/env python3
"""
    Multiple concurrency Write an asynchronous coroutine that
    takes in an integer argument
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Awaits for a random delay between 0 and max_delay """

    relaxing = [await wait_random(max_delay) for _ in range(n)]
    return sorted(relaxing)
