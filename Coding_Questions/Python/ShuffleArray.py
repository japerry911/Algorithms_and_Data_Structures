from typing import List

import pytest


def shuffle(nums: List[int], n: int) -> List[int]:
    pass


def test_shuffle():
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    expected = [2, 3, 5, 4, 1, 7]
    assert shuffle(nums, n) == expected

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    expected = [1, 4, 2, 3, 3, 2, 4, 1]
    assert shuffle(nums, n) == expected

    nums = [1, 1, 2, 2]
    n = 2
    expected = [1, 2, 1, 2]
    assert shuffle(nums, n) == expected


pytest.main(["ShuffleArray.py"])
