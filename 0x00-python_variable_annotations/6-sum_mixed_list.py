#!/usr/bin/env python3
""" Type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function that takes a list of integers and floats and
    returns their sum as a float. """

    cont = 0
    for num in mxd_lst:
        cont += num

    return cont
