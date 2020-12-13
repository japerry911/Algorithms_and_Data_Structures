# ---Spiral Traverse---

from typing import List


def spiral_traverse(array: List[List[int]]) -> List[int]:
    start_row = 0
    end_row = len(array) - 1
    start_column = 0
    end_column = len(array[0]) - 1

    return_list = list()

    while start_row <= end_row and start_column <= end_column:
        for c in range(start_column, end_column + 1):
            return_list.append(array[start_row][c])

        for r in range(start_row + 1, end_row + 1):
            return_list.append(array[r][end_column])

        for c in reversed(range(start_column, end_column)):
            if start_row == end_row:
                break
            return_list.append(array[end_row][c])

        for r in reversed(range(start_row + 1, end_row)):
            if start_column == end_column:
                break
            return_list.append(array[r][start_column])

        start_row += 1
        start_column += 1
        end_row -= 1
        end_column -= 1

        print(return_list)

    return return_list


matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
actual = spiral_traverse(matrix)
print(actual, "\n", expected)
assert actual == expected

matrix2 = [[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
actual = spiral_traverse(matrix2)
print(actual, "\n", expected)
assert actual == expected
