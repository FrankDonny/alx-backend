#!/usr/bin/python3
"""MRUCache module"""

from collections import deque

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """The MRUCache class"""

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
        if key not in self.cache_data.keys():
            self.dict.update({key: 1})
            self.list.append(key)
            print(f"first entry {key}: {self.dict}")
        else:
            self.dict.update({key: self.dict[key] + 1})
            print(f"updated value {key}: {self.dict}")
        self.cache_data[key] = item
        # print(self.cache_data)
        if len(self.cache_data) > self.MAX_ITEMS:
            maxNum = max(self.dict, key=self.dict.get)
            if maxNum in self.list:
                for num in self.list:
                    if num == maxNum:
                        del self.cache_data[num]
                        del self.dict[num]
                        print(f"DISCARD: {num}")
                        break
            else:
                del self.cache_data[maxNum]
                del self.dict[maxNum]
                print(f"removed item {maxNum}: {self.dict}")
                print(F"DISCARD: {maxNum}")

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.dict.update({key: self.dict[key] + 1})
        print(f"get req {key}: {self.dict}")
        return self.cache_data.get(key)


my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
