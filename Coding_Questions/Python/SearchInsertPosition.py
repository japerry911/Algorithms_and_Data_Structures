from typing import List

import pytest


def search_insert(nums: List[int], target: int) -> int:
    """returns index for target number in sorted nums input List
    :param List[int] nums: input list of integers
    :param int target: inputted number that is being inserted into sorted List
    :returns: the index where the target will be placed
    :rtype: int
    """
    for idx, i in enumerate(nums):
        if i == target:
            return idx
        elif i > target:
            return idx

    return len(nums)


def test_search_insert():
    print("search_insert([1, 3, 5, 6], 5) == 2")
    assert search_insert([1, 3, 5, 6], 5) == 2

    print("search_insert([1, 3, 5, 6], 2) == 1")
    assert search_insert([1, 3, 5, 6], 2) == 1

    print("search_insert([1, 3, 5, 6], 7) == 4")
    assert search_insert([1, 3, 5, 6], 7) == 4

    print("search_insert([1, 3, 5, 6], 0) == 0")
    assert search_insert([1, 3, 5, 6], 0) == 0

    print("search_insert([1], 0) == 0")
    assert search_insert([1], 0) == 0


pytest.main(["SearchInsertPosition.py"])
