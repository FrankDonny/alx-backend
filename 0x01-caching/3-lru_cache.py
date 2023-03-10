#!/usr/bin/python3
"""LRUCache module"""

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
        # print(self.dict)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            # print(self.dict)
            least = min(self.dict, key=self.dict.get)  # type: ignore
            if least not in self.list[:self.MAX_ITEMS]:
                newDict = {}
                for i in self.list[:self.MAX_ITEMS]:
                    if i in self.dict.keys():
                        newDict.update({i: self.dict[i]})
                newLeast = min(self.dict, key=self.dict.get)
                del self.cache_data[newLeast]
                del self.dict[newLeast]
                print(f"DISCARD: {newLeast}")
            elif least in self.list[:self.MAX_ITEMS]:
                del self.cache_data[least]
                del self.dict[least]
                print(f"DISCARD: {least}")
            elif self.list[:self.MAX_ITEMS] not in self.dict.keys():
                del self.cache_data[least]
                del self.dict[least]
                print(f"DISCARD: {least}")
        # print(f"least: {min(self.dict, key=self.dict.get)}")

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.dict.update({key: self.dict[key] + 1})
        # print(self.dict)
        return self.cache_data.get(key)
