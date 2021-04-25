from typing import List


def sorted_square_array(array: List[int]) -> List[int]:
    return sorted([pow(element, 2) for element in array])


a = sorted_square_array([-9, 1, 2, 3, 4, 5, 6, 7, 8])
print(a)
assert a == [1, 4, 9, 16, 25, 36, 49, 64, 81]
