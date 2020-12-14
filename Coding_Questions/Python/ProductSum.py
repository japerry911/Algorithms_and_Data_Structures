# ---Product Sum---

from typing import List


def product_sum(array: List, depth: int = 1) -> int:
    running_sum = 0

    for element in array:
        if isinstance(element, list):
            running_sum += product_sum(element, depth + 1)
        else:
            running_sum += element

    return running_sum * depth


# test = [5, [1, [2, 3]]]  # 37
test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
actual = product_sum(test)
expected = 12
print(actual)
assert actual == expected
