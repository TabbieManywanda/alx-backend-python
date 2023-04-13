#!/usr/bin/env python3

'''Import `async_comprehension` from the previous file
and write a coroutine'''

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''write a `measure_runtime` coroutine that will execute
    `async_comprehension` four times in parallel using asyncio.gather
    `measure_runtime` should measure the total runtime and return it'''

    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.perf_counter() - s

    return total_time
