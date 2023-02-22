#!/usr/bin/python3
"""FIFOCache module"""

from collections import deque

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """The FIFOCache class"""

    def __init__(self):
        """initializing of the class, calls the constructor of the
        parent class first"""
        super().__init__()
        self.deque = deque()

    def put(self, key, item):
        """assign to a dictionary key and its item"""
        if key is None or item is None:
            return
        if key not in self.deque:
            self.deque.append(key)
            if len(self.cache_data) == self.MAX_ITEMS:
                for ky in self.cache_data.keys():
                    theKey = self.deque.popleft()
                    del self.cache_data[theKey]
                    print(f"DISCARD: {ky}")
                    break
            self.cache_data[key] = item
        elif key in self.cache_data.keys():
            self.cache_data[key] = item

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
