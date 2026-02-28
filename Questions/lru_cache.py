"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently
Used (LRU) cache.

Implement the LRUCache class:
    - LRUCache(capacity: int) — Initialize the cache with positive size capacity.
    - get(key: int) -> int — Return the value of the key if it exists,
      otherwise return -1.
    - put(key: int, value: int) -> None — Update the value of the key if it
      exists. Otherwise, add the key-value pair to the cache. If the number
      of keys exceeds the capacity, evict the least recently used key.

Both get and put must run in O(1) average time complexity.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)       # returns 1
    cache.put(3, 3)    # evicts key 2
    cache.get(2)       # returns -1
    cache.get(3)       # returns 3
"""


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
