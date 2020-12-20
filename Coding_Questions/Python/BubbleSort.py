# ---Bubble Sort---

from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    counter = 0
    while True:
        swap_occurred = False
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                swap_occurred = True
        if swap_occurred is False:
            break
        counter += 1
    return array


print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
