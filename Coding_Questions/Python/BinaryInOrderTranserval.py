from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: TreeNode, return_list: List[int] = None) \
        -> List[int]:
    if return_list is None:
        return_list = list()

    if root is not None:
        in_order_traversal(root.left, return_list)
        return_list.append(root.val)
        in_order_traversal(root.right, return_list)

    return return_list


