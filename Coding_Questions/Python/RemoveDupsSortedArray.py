from typing import List

import pytest


def remove_duplicates(nums: List[int]) -> int:
    return 1


def test_remove_duplicates():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]

    k = remove_duplicates(nums)

    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]


pytest.main(["RemoveDupsSortedArray.py"])
