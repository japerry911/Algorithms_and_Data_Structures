# ---First Duplicate Value---

from typing import List


def first_duplicate_value(array: List[int]) -> int:
    holding_set = set()

    for element in array:
        if element in holding_set:
            return element
        holding_set.add(element)

    return -1


# def first_duplicate_value(array: List[int]) -> int:
#     holding_dictionary = dict()
#
#     for element in array:
#         if element in holding_dictionary.keys():
#             return element
#         holding_dictionary[element] = True
#
#     return -1


input1 = [2, 1, 5, 2, 3, 3, 4]
expected1 = 2
actual1 = first_duplicate_value(input1)
print(actual1)  # 2
assert actual1 == expected1
