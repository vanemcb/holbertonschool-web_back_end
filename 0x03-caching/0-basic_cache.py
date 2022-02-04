#!/usr/bin/python3
""" BaseCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):

        if key in self.cache_data and key != None:
            return(self.cache_data[key])
        else:
            return None
