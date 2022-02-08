#!/usr/bin/python3
""" LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Class FIFOCache """

    def __init__(self):
        """Initialiaze the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Function put """

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                array_key = self.cache_data.keys()
                print("DISCARD: {}".format(array_key))
                self.cache_data.popitem(last = False)

    def get(self, key):
        """ Function get """
        if key in self.cache_data and key is not None:
            self.cache_data.move_to_end(key)
            return(self.cache_data[key])
        else:
            return None
