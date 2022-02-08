#!/usr/bin/env python3
"""
Module function index_range
"""

import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialiaze the class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """ Function that returns the range of rows """
            assert(type(page) == int and page > 0)
            assert(type(page_size) == int and page_size > 0)
            index, end_index = index_range(page, page_size)
            array_data = self.dataset()
            if index > len(array_data):
                return []
            return array_data[index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Function that returns a dictionary """
        if page != len(self.dataset()):
            next_p = page + 1
        else:
            next_p = None

        if page != 0 and page != 1:
            prev_p = page - 1
        else:
            prev_p = None

        dict_hyper = {"page_size": len(self.get_page(page, page_size)),
                      "page": page,
                      "data": self.get_page(page, page_size),
                      "next_page": next_p,
                      "prev_page": prev_p,
                      "total_pages": round(len(self.dataset()) / page_size)}

        return dict_hyper
