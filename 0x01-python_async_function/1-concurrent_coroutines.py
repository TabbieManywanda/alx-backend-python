#!/usr/bin/env python3

'''imports previous function'''

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''an async routine called `wait_n`
    that takes in 2 int arguments.
    spawn `wait_random` n times with the specified `max_delay`.
    `wait_n` should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort().
    '''
    l = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = [await task for task in asyncio.as_completed(l)]
    return delays
