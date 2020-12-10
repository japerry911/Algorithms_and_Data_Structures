# ---Min Height BST---

import math
from typing import List


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BST(value)
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BST(value)
                    break

        return self


def min_height_bst(array_main: List[int]) -> BST:
    return construct_min_height_bst(array_main, 0, len(array_main) - 1)


# for 1 and 2 solutions:
# def min_height_bst(array_main: List[int]) -> BST:
#     return construct_min_height_bst(array_main, None, 0, len(array_main) - 1)


# Solution 3: O(n) Time | O(n) Space => n is the length of the array
#   ***Same logic as Solution 2, but cleaner code***
def construct_min_height_bst(array_sub: List[int],
                             start_index: int,
                             end_index: int
                             ) -> BST:
    if end_index < start_index:
        return None

    middle_index = (start_index + end_index) // 2

    bst = BST(array_sub[middle_index])

    bst.left = construct_min_height_bst(array_sub,
                                        start_index,
                                        middle_index - 1
                                        )
    bst.right = construct_min_height_bst(array_sub,
                                         middle_index + 1,
                                         end_index
                                         )

    return bst


# # Solution 2: O(n) Time | O(n) Space => n is the length of the array
# def construct_min_height_bst(array_sub: List[int],
#                              bst: BST,
#                              start_index: int ,
#                              end_index: int
#                              ) -> BST:
#     if end_index < start_index:
#         return
#
#     middle_index = (start_index + end_index) // 2
#
#     new_bst_node = BST(array_sub[middle_index])
#     if bst is None:
#         bst = new_bst_node
#     else:
#         if new_bst_node.value < bst.value:
#             bst.left = new_bst_node
#             bst = bst.left
#         else:
#             bst.right = new_bst_node
#             bst = bst.right
#
#     construct_min_height_bst(array_sub, bst, start_index, middle_index - 1)
#     construct_min_height_bst(array_sub, bst, middle_index + 1, end_index)
#
#     return bst


# Solution 1: O(nlog(n)) Time | O(n) Space => n is the length of the array
# def min_height_bst(array_main: List[int]) -> BST:
#     return construct_min_height_bst(array_main, None, 0, len(array_main) - 1)
#
#
# # Solution 1: O(nlog(n)) Time | O(n) Space => n is the length of the array
# def construct_min_height_bst(array_sub: List[int],
#                              bst: BST,
#                              start_index: int ,
#                              end_index: int
#                              ) -> BST:
#     if end_index < start_index:
#         return
#
#     middle_index = (start_index + end_index) // 2
#     value_to_add = array_sub[middle_index]
#
#     if bst is None:
#         bst = BST(value_to_add)
#     else:
#         bst.insert(value_to_add)
#
#     construct_min_height_bst(array_sub, bst, start_index, middle_index - 1)
#     construct_min_height_bst(array_sub, bst, middle_index + 1, end_index)
#
#     return bst


# Testing Methods
def get_tree_height(tree4: BST, height: int = 0) -> int:
    if tree4 is None:
        return height
    left_tree_height = get_tree_height(tree4.left, height + 1)
    right_tree_height = get_tree_height(tree4.right, height + 1)
    return max(left_tree_height, right_tree_height)


def validate_bst(tree3: BST,
                 min_value: int = -math.inf,
                 max_value: int = math.inf
                 ) -> bool:
    if validate_bst_helper(tree3, min_value, max_value) is False:
        return False

    if tree3.left is not None:
        if validate_bst(tree3.left, min_value, tree3.value) is False:
            return False
    if tree3.right is not None:
        if validate_bst(tree3.right, tree3.value, max_value) is False:
            return False

    return True


def validate_bst_helper(tree2: BST,
                        min_value: int = -math.inf,
                        max_value: int = math.inf
                        ) -> bool:
    return min_value <= tree2.value < max_value


def in_order_traverse(tree1: BST, array1: List[int]) -> List[int]:
    if tree1 is not None:
        in_order_traverse(tree1.left, array1)
        array1.append(tree1.value)
        in_order_traverse(tree1.right, array1)
    return array1


# Test
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
tree = min_height_bst(array)

print(validate_bst(tree))  # True
print(get_tree_height(tree))  # 4

in_order = in_order_traverse(tree, [])
print(in_order)  # [1, 2, 5, 7, 10, 13, 14, 15, 22]
assert in_order == [1, 2, 5, 7, 10, 13, 14, 15, 22]
