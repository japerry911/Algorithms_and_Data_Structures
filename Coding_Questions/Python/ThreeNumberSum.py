# ---Three Number Sum---

from typing import List


# Slowest approach O(n^3)
# def three_number_sum(array: List[int], target_sum: int) -> List[List[int]]:
#     return_list = list()
#     array = sorted(array)
#
#     for i in range(len(array)):
#         for c in range(i + 1, len(array)):
#             current_sum = array[i] + array[c]
#             for z in range(c + 1, len(array)):
#                 if current_sum + array[z] == target_sum:
#                     return_list.append([array[i], array[c], array[z]])
#
#     return return_list


def three_number_sum(array: List[int], target_sum: int) -> List[List[int]]:
    return_list = list()
    array = sorted(array)

    for i in range(len(array)):
        left_pointer = i + 1
        right_pointer = len(array) - 1

        while left_pointer < right_pointer:
            current_sum = array[i] + array[left_pointer] + array[right_pointer]
            if current_sum > target_sum:
                right_pointer -= 1
            elif current_sum < target_sum:
                left_pointer += 1
            else:
                return_list.append(
                    [array[i], array[left_pointer], array[right_pointer]]
                )
                left_pointer += 1
                right_pointer -= 1

    return return_list


actual = three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
print(actual)
assert actual == expected
