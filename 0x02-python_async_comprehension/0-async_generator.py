#!/usr/bin/env python3
""" This module contains an asynchronous generator that yield values """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ loops 10 times and generate a random number """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
