#!/usr/bin/env python3
"""
LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Constructor method"""
        super().__init__()
        self.last_put = None

    def put(self, key, item):
        """ To put data to the caching system"""
        data = self.cache_data
        if key is not None and item is not None:
            if len(data) >= self.MAX_ITEMS and key not in data:
                discarded_item = data.pop(self.last_put)
                print("DISCARD: {}".format(self.last_put))
            data[key] = item
            self.last_put = key

    def get(self, key):
        """ To return data from the caching system"""

        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
