# from Questions.lru_cache import LRUCache
from Answers.lru_cache import LRUCache


def test_basic_usage():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_eviction_order():
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.get(1)
    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30


def test_update_existing_key():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(3, 3)
    assert cache.get(2) == -1


def test_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_get_missing_key():
    cache = LRUCache(2)
    assert cache.get(99) == -1
