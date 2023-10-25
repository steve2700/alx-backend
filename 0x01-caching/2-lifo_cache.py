#!/usr/bin/env/python3
"""LIFO Caching"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a class LIFOCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
            the item value for the key key.
            If key or item is None,
            this method should not do anything.
            If the number of items in self.cache_data is
            higher that BaseCaching.MAX_ITEMS:
            you must discard the last item
            put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded
            and following by a new line
            """
        if key is None or item is None:
            return
        # Get the last key (most recently added item)
            last_key = next(reversed(self.cache_data))
            # Remove the last item (LIFO)
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item  # Add the new item to the cache

    def get(self, key):
        """Must return the value in self.cache_data
        linked to key.
        If key is None or if the key doesn’t exis
        t in self.cache_data, return None.
        """
        if key is None or key is not self.cache_data:
            return None
        return self.cache_data[key]
