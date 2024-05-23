#!/usr/bin/env python3
"""
LFU caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching class"""

    def __init__(self):
        """ Constructor method"""

        super().__init__()
        self.lfu_dict = {}

    def put(self, key, item):
        """ To put data to the caching system"""

        data = self.cache_data
        if key and item:
            data[key] = item
            if len(data.keys()) > self.MAX_ITEMS:
                del_key = min(self.lfu_dict, key=self.lfu_dict.get)
                self.lfu_dict.pop(del_key)
                data.pop(del_key)
                print("DISCARD: {}".format(del_key))
            if not (key in self.lfu_dict):
                self.lfu_dict[key] = 0
            else:
                self.lfu_dict[key] += 1

    def get(self, key):
        """ To get data from the caching system"""

        if (key is None) or not (key in self.cache_data):
            return None
        self.lfu_dict[key] += 1
        return self.cache_data.get(key)
