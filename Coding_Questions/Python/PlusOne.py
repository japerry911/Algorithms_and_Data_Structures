from typing import List

import pytest


def plus_one(digits: List[int]) -> List[int]:
    pass


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


pytest.main(["PlusOne.py"])
