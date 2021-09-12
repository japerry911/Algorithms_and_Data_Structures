from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    pass


nums_input = [1, 3, 2, 1]
expected_output = [1, 3, 2, 1, 1, 3, 2, 1]
output = get_concatenation(nums_input)
assert nums_input == expected_output
