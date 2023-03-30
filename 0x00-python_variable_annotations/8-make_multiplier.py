#!/usr/bin/env python3

'''Returns a function'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A function that takes in a float and returns a function
    that multiplies the argument "multiplier" with the callable argument'''
    def val(num: float) -> float:
        '''Multiplies multiplier with num'''
        return num * multiplier
    return val
