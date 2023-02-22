#!/usr/bin/python3
"""FIFOCache module"""

from collections import deque

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """The LRUCache class"""

    def __init__(self):
        """initializing of the class, calls the constructor of the
        parent class first"""
        super().__init__()
        self.dict = {}
        self.list = []

    def put(self, key, item):
        """assign to a dictionary key and its item"""
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.dict.update({key: self.dict[key] + 1})
        else:
            self.dict.update({key: 1})
            self.list.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            least = []
            for ky, value in self.dict.items():
                least.append([ky, value])
            least.sort(key=lambda x: x[1])
            print(least)
            print(self.list)
            for item in self.list:
                for i in least:
                    if i[1] in [i[1] for j in i if j != i[1]]:
                        pass
                    else:
                        

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.dict.update({key: self.dict[key] + 1})
        return self.cache_data.get(key)


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
