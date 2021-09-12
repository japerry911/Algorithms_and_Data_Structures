from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# noinspection PyDefaultArgument
def post_order_traverse(tree: TreeNode) -> List[int]:
    return_array = list()
    return create_output(tree, return_array)


def create_output(tree: TreeNode, array: List[int]) -> List[int]:
    if tree is not None:
        create_output(tree.left, array)
        create_output(tree.right, array)
        array.append(tree.val)
    return array
