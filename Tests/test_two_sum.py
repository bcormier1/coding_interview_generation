# Toggle which implementation to test:
# from Questions.two_sum import two_sum
from Questions.two_sum import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_last_two():
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
