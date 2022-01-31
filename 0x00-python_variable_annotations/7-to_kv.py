#!/usr/bin/env python3
""" Type-annotated function to_kv """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function that takes a string and an int or float
    as arguments and returns a tuple. """

    return (k, v ** 2)
