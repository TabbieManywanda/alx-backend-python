#!/usr/bin/env python3

'''Mixed type annotated function'''

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Function that takes in a list of integers and floats and
    returns their sum as a float'''
    return sum(mxd_list)
