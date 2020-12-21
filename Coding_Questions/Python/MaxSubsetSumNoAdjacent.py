# ---Max Subset Sum No Adjacent---

from typing import List


def max_subset_sum_no_adjacent(array: List[int]) -> int:
    if not len(array):
        return 0

    for i in range(len(array)):
        if i == 0 or i == 1:
            continue
        array[i] += max(array[:i-1])

    return max(array)


print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))  # 330
