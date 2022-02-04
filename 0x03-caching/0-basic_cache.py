#!/usr/bin/python3
""" BaseCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Class BasicCache  """
    def put(self, key, item):
        """ Function put """
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """ Function get """
        if key in self.cache_data and key != None:
            return(self.cache_data[key])
        else:
            return None
