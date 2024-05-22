#!/usr/bin/env python3
""" BasicCache module"""


class BasicCache(BaseCaching):
    """ BasicCache class definition"""

    def __init__(self):
        """ Constructor method"""
        super().__init__()

    def put(self, key, item):
        """ To put data on the caching system"""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ To return a value from the caching system"""

        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
