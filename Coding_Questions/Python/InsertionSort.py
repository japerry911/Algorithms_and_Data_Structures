# ---Insertion Sort---

from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        counter = 0
        for j in range(i - 1, -1, -1):
            if array[i - counter] < array[j]:
                swap(array, i - counter, j)
                counter += 1
            else:
                break

    return array


def insertion_sort2(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
    return array


def swap(array: List[int], i: int, j: int):
    array[i], array[j] = array[j], array[i]


print(insertion_sort2([8, 5, 2, 9, 5, 6, 3]))
