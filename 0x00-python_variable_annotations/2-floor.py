#!/usr/bin/env python3
'''Writing a type annotated floor function'''


def floor(n: float) -> int:
    '''Function that takes in a float parameter
    and returns a rounded down value as int'''
    return int(n // 1)
