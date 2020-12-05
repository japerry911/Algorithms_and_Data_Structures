# ---BST Traversal---

from typing import List


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def in_order_traverse(tree: BST, array: List[int]) -> List[int]:
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


def pre_order_traverse(tree: BST, array: List[int]) -> List[int]:
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)
    return array


def post_order_traverse(tree: BST, array: List[int]) -> List[int]:
    if tree is not None:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)
    return array


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.right = BST(22)

print(in_order_traverse(root, []))  # [1, 2, 5, 5, 10, 15, 22]
assert in_order_traverse(root, []) == [1, 2, 5, 5, 10, 15, 22]

print(pre_order_traverse(root, []))  # [10, 5, 2, 1, 5, 15, 22]
assert pre_order_traverse(root, []) == [10, 5, 2, 1, 5, 15, 22]

print(post_order_traverse(root, []))  # [1, 2, 5, 5, 22, 15, 10]
assert post_order_traverse(root, []) == [1, 2, 5, 5, 22, 15, 10]