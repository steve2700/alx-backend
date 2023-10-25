#!/usr/bion/env/python3
"""LIFO CACHING"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A class LIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value to
        the key in self.cache_data.
        If key or item is None, do nothing.
        If the number of items in
        self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        remove the last item (LIFO algorithm)
        and print DISCARD: with
        the key discarded and a new line.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last key
            last_key = list(self.cache_data.keys())[-1]
            # Remove the last item (LIFO)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """Retrieve the value from self.cache_data linked to the key.
        If key is None or doesn't exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
