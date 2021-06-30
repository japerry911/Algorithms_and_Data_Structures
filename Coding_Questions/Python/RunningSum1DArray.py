from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """Calculates running sum for 1D array for each index
    :param List[int] nums: list of numbers that running sum will be calculated
        on
    :returns: list of running sums
    :rtype: List[int]
    """
    running_sum_amount = 0

    for i in range(len(nums)):
        running_sum_amount += nums[i]
        nums[i] = running_sum_amount

    return nums
