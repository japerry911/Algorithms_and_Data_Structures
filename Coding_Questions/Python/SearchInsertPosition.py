from typing import List

import pytest


def search_insert(nums: List[int], target: int) -> int:
    pass


def test_search_insert():
    print("search_insert([1, 3, 5, 6], 5) == 2")
    assert search_insert([1, 2, 3, 5, 6], 5) == 2

    print("search_insert([1, 3, 5, 6], 2) == 1")
    assert search_insert([1, 3, 5, 6], 2) == 1

    print("search_insert([1, 3, 5, 6], 7) == 4")
    assert search_insert([1, 3, 5, 6], 7) == 4

    print("search_insert([1, 3, 5, 6], 0) == 0")
    assert search_insert([1, 3, 5, 6], 0) == 0

    print("search_insert([1], 0) == 0")
    assert search_insert([1], 0) == 0


pytest.main(["SearchInsertPosition.py"])
