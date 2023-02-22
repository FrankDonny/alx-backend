#!/usr/bin/python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """The BasicCache class"""

    def __init__(self):
        """initializing of the class, calls the constructor of the
        parent class first"""
        super().__init__()

    def put(self, key, item):
        """assign to a dictionary key and its item"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """get the  value of the key"""
        if key is None or key not in self.cache_data.keys():
            return
        else:
            return self.cache_data.get(key)
