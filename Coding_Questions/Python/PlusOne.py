from typing import List

import pytest


def plus_one(digits: List[int], current_idx: int = -1) -> List[int]:
    """Given a non-empty array of decimal digits representing a non-negative
        integer, increment one to the integer.
    :param List[int] digits: the non negative integer input that will be
        incremented
    :param int current_idx: current index that is being incremented
    :returns: incremented non negative integer input value
    :rtype: List[int]
    """
    if abs(current_idx) > len(digits):
        digits.insert(0, 1)
    elif digits[current_idx] < 9:
        digits[current_idx] += 1
    else:
        digits[current_idx] = 0
        plus_one(digits, current_idx - 1)

    return digits


def test_plus_one():
    digits = [1, 2, 3]
    print(f"plus_one({digits}) == [1, 2, 4]")
    assert plus_one(digits) == [1, 2, 4]

    digits = [4, 3, 2, 1]
    print(f"plus_one({digits}) == [4, 3, 2, 2]")
    assert plus_one(digits) == [4, 3, 2, 2]

    digits = [0]
    print(f"plus_one({digits}) == [1]")
    assert plus_one(digits) == [1]

    digits = [1, 9, 9]
    print(f"plus_one({digits}) == [2, 0, 0]")
    assert plus_one(digits) == [2, 0, 0]

    digits = [9, 9, 9]
    print(f"plus_one({digits}) == [1, 0, 0, 0]")
    assert plus_one(digits) == [1, 0, 0, 0]


pytest.main(["PlusOne.py"])
