from Questions.find_outliers import find_outliers
#from Answers.find_outliers import find_outliers


def test_single_outlier():
    assert find_outliers([10, 12, 14, 15, 18, 22, 25, 100]) == [100]


def test_no_outliers():
    assert find_outliers([1, 2, 3, 4, 5, 6, 7, 8]) == []


def test_both_sides():
    values = [-100, 2, 3, 4, 5, 6, 7, 200]
    result = find_outliers(values)
    assert -100 in result
    assert 200 in result


def test_preserves_input_order():
    values = [100, 1, 2, 3, 4, 5, 6, -50]
    result = find_outliers(values)
    assert result == [100, -50]


def test_tight_distribution():
    assert find_outliers([10, 10, 10, 10, 10, 10]) == []
