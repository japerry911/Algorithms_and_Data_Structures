from typing import List

import pytest


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Given an m x n matrix, return all elements of the matrix in spiral
        order
    :param List[List[int] matrix: the 2D matrix that needs to be converted to
        spiral matrix
    :returns: spiral matrix form in 1D List
    :rtype: List[int]
    """
    start_row = 0
    start_column = 0
    end_row = len(matrix) - 1
    end_column = len(matrix[0]) - 1
    output = list()

    while start_row <= end_row and start_column <= end_column:
        for c in range(start_column, end_column + 1):
            output.append(matrix[start_row][c])

        for r in range(start_row + 1, end_row + 1):
            output.append(matrix[r][end_column])

        if start_row != end_row:
            for c in reversed(range(start_column, end_column)):
                output.append(matrix[end_row][c])

        if start_column != end_column:
            for r in reversed(range(start_row + 1, end_row)):
                output.append(matrix[r][start_column])

        start_row += 1
        end_column -= 1
        end_row -= 1
        start_column += 1

    return output


def test_spiral_order():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order(matrix) == expected

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order(matrix) == expected


pytest.main(["SpiralMatrix.py"])
