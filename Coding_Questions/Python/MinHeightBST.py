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


def min_height_bst(input_list: List[int], bst_tree: BST = None) -> BST:
    middle_index = math.floor(len(input_list) / 2)
    middle_value = input_list[middle_index]

    if bst_tree is None:
        bst_tree = BST(middle_value)

    left_sub_tree = input_list[0:middle_index]

    right_sub_tree = input_list[middle_index + 1:]


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

# print(validate_bst(tree))  # True
# print(get_tree_height(tree))  # 4
#
# in_order = in_order_traverse(tree, [])
# print(in_order)  # [1, 2, 5, 7, 10, 13, 14, 15, 22]
# assert in_order == [1, 2, 5, 7, 10, 13, 14, 15, 22]
