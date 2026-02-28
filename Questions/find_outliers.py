"""
Find Outliers (IQR Method)

Given a list of numerical values, return a list of values that are
outliers using the interquartile range (IQR) method.

A value is an outlier if it falls below Q1 - 1.5 * IQR or above
Q3 + 1.5 * IQR, where:
    - Q1 is the 25th percentile
    - Q3 is the 75th percentile
    - IQR = Q3 - Q1

Use linear interpolation for percentile calculation (matching numpy's
default behavior). Do not use pandas, numpy, or any external libraries.

Return the outliers in the order they appear in the input.

Example:
    Input: values = [10, 12, 14, 15, 18, 22, 25, 100]
    Output: [100]

Constraints:
    - len(values) >= 4
    - All values are finite numbers
"""


def find_outliers(values: list[float]) -> list[float]:
    pass