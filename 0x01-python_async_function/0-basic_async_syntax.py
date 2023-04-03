#!usr/bin/env python3

'''an asynchronous coroutine that
takes in an integer argument'''

import asyncio
import random
from typing import Callable


async def wait_random(max_delay: int = 10) -> float:
    '''an asynchronous coroutine that
    takes in an integer argument
    'max_delay', with a default value of 10'''
    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)

    return wait_time
