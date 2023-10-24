## Caching System Project
This project implements various caching algorithms in Python and provides a basic caching system. The implemented caching algorithms include FIFO (First-In-First-Out), LIFO (Last-In-First-Out), LRU (Least Recently Used), MRU (Most Recently Used), and LFU (Least Frequently Used). Additionally, there is a BasicCache class that provides a simple caching system without any size limit.

## Table of Contents
Overview
Implemented Caching Algorithms
BasicCache
Requirements
Usage
License
Overview
A caching system is a technology used to temporarily store frequently accessed or computed data in a fast storage location. Caching helps improve the performance and efficiency of applications by reducing the need to fetch the data from slower storage sources. This project explores different caching algorithms and provides implementations for educational purposes.

## Implemented Caching Algorithms
FIFO (First-In-First-Out)
FIFO is a caching algorithm that evicts the oldest entry first. In other words, the item that has been in the cache the longest is removed to make space for new items.

LIFO (Last-In-First-Out)
LIFO is a caching algorithm that evicts the newest entry first. The item that has been added most recently is removed to accommodate new items.

LRU (Least Recently Used)
LRU is a caching algorithm that removes the least recently used items first. It keeps track of the order in which each item is accessed and removes the item that has not been accessed for the longest time.

MRU (Most Recently Used)
MRU is a caching algorithm that removes the most recently used items first. It prioritizes recently accessed items over less recently accessed items.

LFU (Least Frequently Used)
LFU is a caching algorithm that removes the least frequently used items first. It keeps track of how often an item is accessed and removes the item with the lowest access frequency.

## BasicCache
The Basic Cache 
Cache class provides a simple caching system without any size limit. It allows adding items with corresponding keys and retrieving items based on keys. If a key or item is None, the system does not store the data.

## Usage
To use the caching algorithms, instantiate the respective classes and use the put method to add items to the cache. You can retrieve items from the cache using the get method. For example:

## python
Copy code
# Example usage of BasicCache
from basic_cache import BasicCache
## Code 
my_cache = BasicCache()
my_cache.put("key", "value")
result = my_cache.get("key")
print(result)  # Output: value
Requirements
Python 3.7
pycodestyle 2.5 (for code style checks)





