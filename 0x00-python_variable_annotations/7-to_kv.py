#!/usr/bin/env python3

'''Function that returns a tuple'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that takes in a string and int/float as arguments
    and returns a tuple'''
    ans: float = v ** 2
    return (k, ans)
