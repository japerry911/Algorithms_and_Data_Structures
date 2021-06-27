from typing import List

import pytest


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    pass


def test_merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1,2,2,3,5,6]")
    assert merge(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1]")
    assert merge(nums1, m, nums2, n) == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1]")
    assert merge(nums1, m, nums2, n) == [1]


pytest.main(["MergeSortedArray.py"])
