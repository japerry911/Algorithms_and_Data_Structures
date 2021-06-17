from typing import List

import pytest


def remove_duplicates(nums: List[int]) -> int:
    """removes duplicates from a sorted array with moving them to front and
        not removing any elements and returning length of unique elements
    :param List[int] nums: sorted array input
    :returns: number representing the length of the unique array
    :rtype: int
    """
    look_up_dict = dict()
    current_iterate_idx = 0
    current_nums_idx = 0

    while current_iterate_idx < len(nums):
        if nums[current_iterate_idx] in look_up_dict.keys():
            current_iterate_idx += 1
            continue

        look_up_dict[nums[current_iterate_idx]] = True
        nums[current_nums_idx] = nums[current_iterate_idx]
        current_nums_idx += 1
        current_iterate_idx += 1

    return current_nums_idx


def test_remove_duplicates():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]

    k = remove_duplicates(nums)

    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]


pytest.main(["RemoveDupsSortedArray.py"])
