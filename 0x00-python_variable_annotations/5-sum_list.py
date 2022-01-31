#!/usr/bin/env python3
""" Type-annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function that takes a list of floats as argument and
    returns  their sum as a float. """

    cont = 0
    for num in input_list:
        cont += num

    return cont
