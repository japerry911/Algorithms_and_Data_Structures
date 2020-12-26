# ---Powerset---

from typing import List


def powerset(array: List[int]) -> List[List[int]]:
    powersets = [[]]

    for element in array:
        powersets.append([element])
        for i in range (1, len(powersets) - 1):
            new_element = powersets[i]
            powersets.append(new_element + [element])

    return powersets


def check_if_2d_lists_are_equal(
        list1: List[List[int]], list2: List[List[int]]
) -> bool:
    return len(list1) == len(list2) and sorted(list1) == sorted(list2)


input1 = [1, 2, 3]
expected_output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
actual = powerset(input1)
print(f"EXPECTED:\t{expected_output}")
print("----------------------------")
print(f"ACTUAL:\t\t{actual}")
assert check_if_2d_lists_are_equal(actual, expected_output)
