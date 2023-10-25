#!/usr/bion/env/python3
"""MRU CACHING"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """a class MRUCache that inherits
    from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """Assign the item value to
        the key in self.cache_data.
        If key or item is None, do nothing.
        If the number of items in
        self.cache_data is higher
        than BaseCaching.MAX_ITEMS,
        you must discard the most
        recently used item (MRU algorithm)
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the most key first key in key_order list)
            mru_key = self.key_order.pop()
            # Remove the most recently used item
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """Retrieve the value from self.cache_data linked to the key.
        If key is None or doesn't exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update key_order: remove the key and add it to the end (most recently
        # used)
        self.key_order.remove(key)
        self.key_order.append(key)

        return self.cache_data[key]
