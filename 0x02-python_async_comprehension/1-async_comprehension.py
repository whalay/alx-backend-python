#!/usr/bin/env python3
""" This module contains an asynchronous function """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ performs an asynchronous list comprehension """

    return [i async for i in async_generator()]
