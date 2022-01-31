#!/usr/bin/env python3
""" Type-annotated function element_length"""
from typing import List, Union, Tuple, Callable, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function that returns the length of a list """
    return [(i, len(i)) for i in lst]
