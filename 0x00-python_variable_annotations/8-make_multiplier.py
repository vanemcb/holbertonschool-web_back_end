#!/usr/bin/env python3
""" Type-annotated function make_multiplier """
from audioop import mul
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function that takes a float and as argument
    and returns a function that multiplies a float by multipliere. """
    def f(num: float) -> float:
        return num * multiplier

    return f
