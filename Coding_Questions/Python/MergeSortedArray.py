from typing import List

import pytest


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """merge sorted arrays in-place
    :param List[int] nums1: nums1 List sorted
    :param int m: number of elements in nums1
    :param List[int] nums2: nums2 List sorted
    :param int n: number of elements in nums2
    :returns: nothing, sorts nums1 in-place
    :rtype: None
    """
    idx_m = m - 1
    idx_n = n - 1
    main_idx = m + n - 1

    while idx_m >= 0 and idx_n >= 0:
        if nums1[idx_m] > nums2[idx_n]:
            nums1[main_idx] = nums1[idx_m]
            main_idx -= 1
            idx_m -= 1
        else:
            nums1[main_idx] = nums2[idx_n]
            main_idx -= 1
            idx_n -= 1

    nums1[:idx_n + 1] = nums2[:idx_n + 1]


def test_merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1,2,2,3,5,6]")
    merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1]")
    merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(f"merge({nums1}, {m}, {nums2}, {n}) == [1]")
    merge(nums1, m, nums2, n)
    assert nums1 == [1]


pytest.main(["MergeSortedArray.py"])
