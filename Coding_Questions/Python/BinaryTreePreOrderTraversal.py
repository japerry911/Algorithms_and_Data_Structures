from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root: TreeNode) -> List[int]:
    return_array = list()
    return create_output(root, return_array)


def create_output(tree: TreeNode, array: List[int]) -> List[int]:
    if tree is not None:
        array.append(tree.val)
        create_output(tree.left, array)
        create_output(tree.right, array)
    return array
