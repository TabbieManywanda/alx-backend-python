#!/usr/bin/env python3

'''Create a `measure_time` function'''

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Create a `measure_time` function with int args n and max_delay.
    measures the total execution time for `wait_n(n, max_delay)`
    returns total_time / n.
    Your function should return a float.'''
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s

    return total_time / n
