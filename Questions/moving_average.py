"""
Moving Average

Given a list of numbers and a window size k, return a list of the simple
moving averages. Each element in the output is the mean of the current
element and the previous k-1 elements. For positions where the full window
is not yet available, compute the mean of all available elements up to
that point.

Do not use pandas or any external libraries — use only the Python
standard library.

Example:
    Input: values = [1, 3, 5, 7, 9], k = 3
    Output: [1.0, 2.0, 3.0, 5.0, 7.0]

    Explanation:
        [1] -> 1.0
        [1, 3] -> 2.0
        [1, 3, 5] -> 3.0
        [3, 5, 7] -> 5.0
        [5, 7, 9] -> 7.0
"""


def moving_average(values: list[float], k: int) -> list[float]:
    pass
