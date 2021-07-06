from typing import List

import pytest


def spiral_order(matrix: List[List[int]]) -> List[int]:
    pass


def test_spiral_order():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order(matrix) == expected

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order(matrix) == expected


pytest.main(["SpiralMatrix.py"])
