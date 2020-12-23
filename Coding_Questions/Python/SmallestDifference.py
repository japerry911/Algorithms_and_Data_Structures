# ---Smallest Difference---

from typing import List




# iterate through every possible pair (slow)
def smallest_difference(array1: List[int], array2: List[int]) -> List[int]:
    return_pair = None

    for num1 in array1:
        for num2 in array2:
            if return_pair is None:
                return_pair = [num1, num2]
            elif calculate_difference(
                    return_pair[0], return_pair[1]
            ) > calculate_difference(num1, num2):
                return_pair = [num1, num2]

    return return_pair


def calculate_difference(num1: int, num2: int) -> int:
    return abs(num1 - num2)


print(
    smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
)  # [28, 26]
