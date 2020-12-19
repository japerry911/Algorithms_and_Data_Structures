# ---Binary Search---

from typing import List


def binary_search(array: List[int], target: int) -> int:
    return binary_search_helper(array, target, 0, len(array) - 1)


# def binary_search_helper(
#         array: List[int],
#         target: int,
#         left_pointer: int,
#         right_pointer: int
# ):
#     while left_pointer < right_pointer:
#         # // => floor division operator
#         middle_point = (left_pointer + right_pointer) // 2
#         if array[middle_point] == target:
#             return middle_point
#         elif array[middle_point] > target:
#             right_pointer = middle_point - 1
#         elif array[middle_point] < target:
#             left_pointer = middle_point + 1
#     return -1 if array[left_pointer] != target else left_pointer

def binary_search_helper(
        array: List[int],
        target: int,
        left_pointer: int,
        right_pointer: int
):
    while left_pointer <= right_pointer:
        # // => floor division operator
        middle_point = (left_pointer + right_pointer) // 2
        if array[middle_point] == target:
            return middle_point
        elif array[middle_point] > target:
            right_pointer = middle_point - 1
        elif array[middle_point] < target:
            left_pointer = middle_point + 1
    return -1


print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))  # 3
