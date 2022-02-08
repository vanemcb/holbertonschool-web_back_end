#!/usr/bin/env python3
""" Module function index_range """


def index_range(page: int, page_size: int) -> tuple:
    """ Function that takes two integer arguments and return
    a tuple of size two containing a start index and an end index """

    index = (page - 1) * page_size
    end_index = index + page_size
    return (index, end_index)
