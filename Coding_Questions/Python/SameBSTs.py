# ---Same BSTs---

from typing import List


# class BST:
#     def __init__(self, value: int):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, value: int):
#         current_node = self
#
#         while True:
#             if value < current_node.value:
#                 if current_node.left is None:
#                     current_node.left = BST(value)
#                     break
#                 else:
#                     current_node = current_node.left
#             else:
#                 if current_node.right is None:
#                     current_node.right = BST(value)
#                     break
#                 else:
#                     current_node = current_node.right
#
#         return self
#
#
# def in_order_traversal(tree: BST, array: List[int]) -> List[int]:
#     if tree is not None:
#         in_order_traversal(tree.left, array)
#         array.append(tree.value)
#         in_order_traversal(tree.right, array)
#     return array
#
#
# def same_bsts(array1: List[int], array2: List[int]) -> bool:
#     if not len(array1) or not len(array2) or (len(array1) != len(array2)):
#         return False
#
#     bst1 = BST(array1.pop(0))
#     bst2 = BST(array2.pop(1))
#
#     for i in range(len(array1)):
#         bst1.insert(array1[i])
#         bst2.insert(array2[i])
#
#     bst1_traversal = in_order_traversal(bst1, [])
#     bst2_traversal = in_order_traversal(bst2, [])
#
#     return bst1_traversal == bst2_traversal


def same_bsts(array1: List[int], array2: List[int]) -> bool:
    if not len(array1) or not len(array2):
        return True
    elif array1[0] != array2[0] or len(array1) != len(array2):
        return False
    elif len(array1) == 1 and len(array2) == 1:
        return array1[0] == array2[0]

    root_value1 = array1.pop(0)
    root_value2 = array2.pop(0)

    left_subtree_values1 = list(filter(lambda x: x < root_value1, array1))
    left_subtree_values2 = list(filter(lambda x: x < root_value2, array2))
    right_subtree_values1 = list(filter(lambda x: x >= root_value1, array1))
    right_subtree_values2 = list(filter(lambda x: x >= root_value2, array2))

    if sorted(left_subtree_values1) != sorted(left_subtree_values2):
        return False
    if sorted(right_subtree_values1) != sorted(right_subtree_values2):
        return False

    return same_bsts(left_subtree_values1, left_subtree_values2) and \
           same_bsts(right_subtree_values1, right_subtree_values2)


array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
actual = same_bsts(array_one, array_two)
print(actual)
assert actual
