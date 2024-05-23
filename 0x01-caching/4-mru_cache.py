#!/usr/bin/env python3
"""
MRU caching modul
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Class for LRU Caching"""

    def __init__(self):
        """ Constructor method"""
        super().__init__()
        self.mru_dict = OrderedDict()

    def put(self, key, item):
        """ To put data to the caching system"""

        data = self.cache_data
        if key and item:
            self.mru_dict[key] = item
            data[key] = item

        if len(data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.mru_dict))
            data.pop(first_key)
            print("DISCARD: {}".format(first_key))

        if len(self.mru_dict) > BaseCaching.MAX_ITEMS:
            self.mru_dict.popitem(last=False)

        self.mru_dict.move_to_end(key, False)

    def get(self, key):
        """ To get data from the caching system"""

        if key in self.cache_data:
            self.mru_dict.move_to_end(key, False)
            return self.cache_data[key]
        return None
