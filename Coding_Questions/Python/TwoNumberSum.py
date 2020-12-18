from typing import List


# ---Two Number Sum---

# Solution 1: O(n^2) Time | O(1) Space
# def two_number_sum(array: List[int], target_sum: int) -> List[int]:
#     for main_index, i in enumerate(array):
#         for sub_index, c in enumerate(array):
#             if main_index == sub_index:
#                 continue
#             elif i + c == target_sum:
#                 return [i, c]
#     return list()


# Solution 2: O(n) Time | O(n) Space
# def two_number_sum(array: List[int], target_sum: int) -> List[int]:
#     nums = dict()
#     for num in array:
#         potential_match = target_sum - num
#         if potential_match in nums:
#             return [potential_match, num]
#         else:
#             nums[num] = True
#     return list()


# Solution 3: O(nlog(n)) Time | O(1) Space
def two_number_sum(array: List[int], target_sum: int) -> List[int]:
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
    return list()


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
# non-specific ordering => [-1, 11]
