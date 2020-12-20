# ---Selection Sort---

from typing import List


def selection_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        pointer = i
        for c in range(i + 1, len(array)):
            if array[pointer] > array[c]:
                pointer = c
        swap(array, i, pointer)
    return array


def swap(array: List[int], i: int, j: int):
    array[i], array[j] = array[j], array[i]


print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
