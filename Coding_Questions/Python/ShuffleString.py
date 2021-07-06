from typing import List

import pytest


def restore_string(s: str, indices: List[int]) -> str:
    """Given a list of indices and a shuffled string, restore the string
    :param str s: the inputted shuffled string
    :param List[int] indices: the inputted indices of the un-shuffled string
    :returns: the restored un-shuffled string
    :rtype: str
    """
    restored_list = [""] * len(indices)

    for i in range(len(indices)):
        restored_list[indices[i]] = s[i]

    return "".join(restored_list)


def test_restore_string():
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    expected = "leetcode"
    assert restore_string(s, indices) == expected

    s = "abc"
    indices = [0, 1, 2]
    expected = "abc"
    assert restore_string(s, indices) == expected

    s = "aiohn"
    indices = [3, 1, 4, 2, 0]
    expected = "nihao"
    assert restore_string(s, indices) == expected

    s = "aaiougrt"
    indices = [4, 0, 2, 6, 7, 3, 1, 5]
    expected = "arigatou"
    assert restore_string(s, indices) == expected

    s = "art"
    indices = [1, 0, 2]
    expected = "rat"
    assert restore_string(s, indices) == expected


pytest.main(["ShuffleString.py"])
