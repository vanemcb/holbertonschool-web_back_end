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
            """ Function that returns the range of rows
            """
            assert(type(page) == int and page > 0)
            assert(type(page_size) == int and page_size > 0)
            index, end_index = index_range(page, page_size)

            if index > 19419 or end_index > 19419:
                return []

            array_rows = []
            array_data = self.dataset()

            for i in range(index, end_index):
                array_rows.append(array_data[i])

            return array_rows