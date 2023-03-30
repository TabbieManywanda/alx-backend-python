#!/usr/bin/env python3

'''Annotating a function'''

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''A function taking in an iterable list and returning
    a list containing a tuple'''
    return [(i, len(i)) for i in lst]
