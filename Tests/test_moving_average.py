# from Questions.moving_average import moving_average
from Answers.moving_average import moving_average


def test_basic():
    assert moving_average([1, 3, 5, 7, 9], 3) == [1.0, 2.0, 3.0, 5.0, 7.0]


def test_window_equals_length():
    result = moving_average([2, 4, 6], 3)
    assert result == [2.0, 3.0, 4.0]


def test_window_of_one():
    assert moving_average([10, 20, 30], 1) == [10.0, 20.0, 30.0]


def test_constant_values():
    assert moving_average([5, 5, 5, 5], 2) == [5.0, 5.0, 5.0, 5.0]


def test_single_element():
    assert moving_average([42], 3) == [42.0]
