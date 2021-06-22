from typing import List

import pytest


def max_sub_array(nums: List[int]) -> int:
    pass


def test_max_sub_array():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"max_sub_array({nums}) == 6")
    assert max_sub_array(nums) == 6

    nums = [1]
    print(f"max_sub_array({nums}) == 1")
    assert max_sub_array(nums) == 1

    nums = [5, 4, -1, 7, 8]
    print(f"max_sub_array({nums}) == 23")
    assert max_sub_array(nums) == 23


pytest.main(["MaximumSubArray.py"])
