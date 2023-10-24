#!/usr/bin/env python3
"""Basic class module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class BasicCache that inherits
    from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        If key is None or key doesn't exist, return None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
