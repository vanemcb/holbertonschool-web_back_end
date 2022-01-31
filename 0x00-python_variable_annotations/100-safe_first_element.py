#!/usr/bin/env python3
""" Type-annotated function safe_first_element"""
from typing import List, Union, Tuple, Callable, Sequence, Iterable, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function that returns the first element of a list """
    if lst:
        return lst[0]
    else:
        return None
