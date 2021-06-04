def twoSum(nums: List[int], target: int) -> List[int]:
    total = 0
    for i in range(len(nums)):
        for r in range(i + 1, len(nums)):
            if nums[i] + nums[r] == target:
                return [i, r]
    return list()