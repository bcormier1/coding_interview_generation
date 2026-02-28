# from Questions.group_anagrams import group_anagrams
from Answers.group_anagrams import group_anagrams


def _sort_groups(groups: list[list[str]]) -> list[list[str]]:
    """Sort for order-independent comparison."""
    return sorted(sorted(g) for g in groups)


def test_basic():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert _sort_groups(result) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_single_string():
    assert group_anagrams(["a"]) == [["a"]]


def test_all_anagrams():
    result = group_anagrams(["abc", "bca", "cab"])
    assert _sort_groups(result) == [["abc", "bca", "cab"]]


def test_empty_strings():
    result = group_anagrams(["", ""])
    assert _sort_groups(result) == [["", ""]]


def test_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    assert _sort_groups(result) == [["abc"], ["def"], ["ghi"]]
