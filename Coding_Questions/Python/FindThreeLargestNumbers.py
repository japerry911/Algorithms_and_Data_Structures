# ---Find Three Largest Numbers---

from typing import List


# Solution 1: O(n) Time | O(1) Space
def find_three_largest_numbers(array: List[int]) -> List[int]:
    three_largest = [None, None, None]
    for element in array:
        update_largest(three_largest, element)
    return three_largest


def update_largest(three_largest: List[int], element: int):
    if three_largest[2] is None or element > three_largest[2]:
        shift_and_update(three_largest, 2, element)
    elif three_largest[1] is None or element > three_largest[1]:
        shift_and_update(three_largest, 1, element)
    elif three_largest[0] is None or element > three_largest[0]:
        shift_and_update(three_largest, 0, element)


def shift_and_update(three_largest: List[int], idx: int, element: int):
    for i in range(idx):
        three_largest[i] = three_largest[i + 1]
    three_largest[idx] = element


input1 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
expected1 = [18, 141, 541]
actual1 = find_three_largest_numbers(input1)
print(f"EXPECTED:\t{expected1}")
print(f"ACTUAL\t\t{actual1}")
