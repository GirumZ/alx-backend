#!/usr/bin/env python3
"""
LRU caching modul
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Class for LRU Caching"""

    def __init__(self):
        """ Constructor method"""
        super().__init__()
        self.lru_dict = OrderedDict()

    def put(self, key, item):
        """ To put data to the caching system"""

        data = self.cache_data
        if key and item:
            self.lru_dict[key] = item
            self.lru_dict.move_to_end(key)
            data[key] = item

        if len(data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.lru_dict))
            data.pop(first_key)
            print("DISCARD: {}".format(first_key))

        if len(self.lru_dict) > BaseCaching.MAX_ITEMS:
            self.lru_dict.popitem(last=False)

    def get(self, key):
        """ To get data from the caching system"""

        if key in self.cache_data:
            self.lru_dict.move_to_end(key)
            return self.cache_data[key]
        return None
