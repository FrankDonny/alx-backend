#!/usr/bin/python3
"""LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """The LIFOCache class"""

    def __init__(self):
        """initializing of the class, calls the constructor of the
        parent class first"""
        super().__init__()
        self.deque = []

    def put(self, key, item):
        """assign to a dictionary key and its item"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.deque.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.deque.pop(-2)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
