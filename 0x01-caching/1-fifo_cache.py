#!/usr/bin/env/python3
"""Fifo caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):

    """A class FIFOCache that inherits from
    BaseCaching and is a caching system.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value to the dictionary
        self.cache_data for the given key.
        If key or item is None, do nothing.
        If the number of items in self.cache_data is
        higher than BaseCaching.MAX_ITEMS,
        remove the first item put in the cache (FIFO algorithm).
        Print DISCARD: with the key discarded and followed by a new line.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first key (oldest item)
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]  # Remove the first item (FIFO)
            print("DISCARD:", first_key)

        self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """Retrieve the item from the cache
        based on the provided key.
        If key is None or if the key doesn’t
        exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
