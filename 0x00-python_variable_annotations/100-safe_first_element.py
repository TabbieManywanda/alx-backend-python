#!/usr/bin/env python3

'''Augmenting given code'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''A function that takes in a list and
    returns the first element of the list or
    None if no list is passed'''
    if lst:
        return lst[0]
    else:
        return None
