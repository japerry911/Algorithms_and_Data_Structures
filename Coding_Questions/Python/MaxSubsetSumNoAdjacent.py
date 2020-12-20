# ---Max Subset Sum No Adjacent---

from typing import List


def max_subset_sum_no_adjacent(array: List[int]) -> int:
    if not len(array):
        return 0


print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))  # 330
