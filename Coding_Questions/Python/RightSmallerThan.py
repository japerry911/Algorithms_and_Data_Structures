# ---Right Smaller Than---

from typing import List


class SpecialBST:
    def __init__(self, value: int, idx: int, num_smaller_at_insert_time: int):
        self.value = value
        self.idx = idx
        self.num_smaller_at_insert_time = num_smaller_at_insert_time
        self.left_subtree_size = 0
        self.left = None
        self.right = None

    def insert(
            self, value: int, idx: int, num_smaller_at_insert_time: int = 0
    ):
        if value < self.value:
            self.left_subtree_size += 1
            if self.left is None:
                self.left = SpecialBST(value, idx, num_smaller_at_insert_time)
            else:
                self.left.insert(value, idx, num_smaller_at_insert_time)
        else:
            num_smaller_at_insert_time += self.left_subtree_size
            if value > self.value:
                num_smaller_at_insert_time += 1
            if self.right is None:
                self.right = SpecialBST(value, idx, num_smaller_at_insert_time)
            else:
                self.right.insert(value, idx, num_smaller_at_insert_time)


# Solution 2: O(n(log(n)) Time | O(n) Space
def right_smaller_than(array: List[int]) -> List[int]:
    if not len(array):
        return []

    last_idx = len(array) - 1
    bst = SpecialBST(array[last_idx], last_idx, 0)
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i)

    right_smaller_counts = array[:]
    get_right_smaller_counts(bst, right_smaller_counts)

    return right_smaller_counts


def get_right_smaller_counts(bst: SpecialBST, right_smaller_counts: List[int]):
    if bst is None:
        return
    right_smaller_counts[bst.idx] = bst.num_smaller_at_insert_time
    get_right_smaller_counts(bst.left, right_smaller_counts)
    get_right_smaller_counts(bst.right, right_smaller_counts)


# # Solution 1: Time O(n^2) | Space O(n)
# def right_smaller_than(array: List[int]) -> List[int]:
#     return_array = list()
#
#     for i in range(len(array)):
#         smaller_thans = 0
#         for j in range(i + 1, len(array)):
#             if array[i] > array[j]:
#                 smaller_thans += 1
#         return_array.append(smaller_thans)
#
#     return return_array
