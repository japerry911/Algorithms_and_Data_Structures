# ---Smallest Difference---

import math
from typing import List


def smallest_difference(array1: List[int], array2: List[int]) -> List[int]:
    array1 = sorted(array1)
    array2 = sorted(array2)

    current_smallest_difference = [None, math.inf]

    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(array1) and pointer2 < len(array2):
        pairs_difference = calculate_difference(
            array1[pointer1], array2[pointer2]
        )

        if pairs_difference == 0:
            return [array1[pointer1], array2[pointer2]]

        if pairs_difference < current_smallest_difference[1]:
            current_smallest_difference = [
                [array1[pointer1], array2[pointer2]], pairs_difference
            ]

        if array1[pointer1] < array2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1

    return current_smallest_difference[0]


def calculate_difference(num1: int, num2: int) -> int:
    return abs(num1 - num2)


# # iterate through every possible pair (slow)
# def smallest_difference(array1: List[int], array2: List[int]) -> List[int]:
#     return_pair = None
#
#     for num1 in array1:
#         for num2 in array2:
#             if return_pair is None:
#                 return_pair = [num1, num2]
#             elif calculate_difference(
#                     return_pair[0], return_pair[1]
#             ) > calculate_difference(num1, num2):
#                 return_pair = [num1, num2]
#
#     return return_pair
#
#
# def calculate_difference(num1: int, num2: int) -> int:
#     return abs(num1 - num2)


print(
    smallest_difference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123],
                        [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530])
)  # [28, 26]
