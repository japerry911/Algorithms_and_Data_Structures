from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    return nums * 2


nums_input = [1, 3, 2, 1]
expected_output = [1, 3, 2, 1, 1, 3, 2, 1]
output = get_concatenation(nums_input)
print(expected_output, ' == ', output)
assert expected_output == output
