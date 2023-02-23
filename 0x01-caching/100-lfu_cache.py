#!/usr/bin/python3
""" 4. MRU and LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache that inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.freq = {}
        self.min_freq = 0

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        # Check if key exists in cache
        if key in self.cache_data:
            # Update item and frequency
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            # Add new item to cache
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard LFU item
                lfu_keys = [k for k in self.freq.keys() if self.freq[k]
                            == self.min_freq]
                if len(lfu_keys) > 1:
                    lru_key = self.lru_key(lfu_keys)
                    del self.cache_data[lru_key]
                    del self.freq[lru_key]
                else:
                    del self.cache_data[lfu_keys[0]]
                    del self.freq[lfu_keys[0]]
                print("DISCARD:", lfu_keys[0])
                self.min_freq = min(self.freq.values()) if len(
                    self.freq) > 0 else 0

            self.cache_data[key] = item
            self.freq[key] = 1
            self.min_freq = 1

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency
        self.freq[key] += 1
        if self.freq[key] > self.min_freq:
            self.min_freq = self.freq[key]

        return self.cache_data[key]

    def lru_key(self, keys):
        """ Find the least recently used key """
        lru_key = None
        for k in keys:
            if lru_key is None or self.last_accessed[k] < self.last_accessed[lru_key]:
                lru_key = k
        return lru_key
