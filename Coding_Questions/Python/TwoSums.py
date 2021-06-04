from typing import List


# Brute Force Method
# def twoSum(nums: List[int], target: int) -> List[int]:
#     total = 0
#     for i in range(len(nums)):
#         for r in range(i + 1, len(nums)):
#             if nums[i] + nums[r] == target:
#                 return [i, r]
#     return list()


def two_sum(nums: List[int], target: int) -> List[int] or None:
    """
    calculates the two indices whose values add up to input target
    :param List[int] nums: the list of numbers
    :param int target: the target number
    :return: A list of the indices whose values add up to target
    :rtype: List[int] or None
    """
    nums_dict = dict()

    for idx, num in enumerate(nums):
        if target - num in nums_dict.keys():
            return [nums_dict[target - num], idx]

        nums_dict[num] = idx

    return None


print(two_sum([3,2,3], 6), "==", [0, 2])
