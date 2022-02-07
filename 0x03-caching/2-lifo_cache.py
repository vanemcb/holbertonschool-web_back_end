#!/usr/bin/python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class FIFOCache """

    def __init__(self):
        """Initialiaze the class"""
        super().__init__()

    def put(self, key, item):
        """ Function put """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                array_key = sorted(self.cache_data.keys())
                print("DISCARD: {}".format(array_key[len(array_key) - 2]))
                self.cache_data.pop(array_key[len(array_key) - 2])

    def get(self, key):
        """ Function get """
        if key in self.cache_data and key is not None:
            return(self.cache_data[key])
        else:
            return None
