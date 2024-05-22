#!/usr/bin/env python3
"""
FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class"""

    def __init__(self):
        """ Constructor method"""
        super().__init__()

    def put(self, key, item):
        """ To put data to the caching system"""
        data = self.cache_data
        if key is not None and item is not None:
            if len(data) >= BaseCaching.MAX_ITEMS and key not in data:
                first_key = next(iter(data))
                # first_item is also discarded item
                first_item = data.pop(first_key)
                print("DISCARD: {}".format(first_key))

            data[key] = item

    def get(self, key):
        """ To return data from the caching system"""

        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
