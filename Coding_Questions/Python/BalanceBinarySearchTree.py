# ---Balance Binary Search Tree---

from typing import List


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left=None,
            right=None
    ):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root: TreeNode) -> TreeNode:
    tree_values_list = in_order_traverse(root, [])
    return construct_balanced_bst(tree_values_list,
                                  0,
                                  len(tree_values_list) - 1)


def in_order_traverse(tree: TreeNode, array: List[int]) -> List[int]:
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.val)
        in_order_traverse(tree.right, array)
    return array


def construct_balanced_bst(array_sub: List[int],
                           start_index: int,
                           end_index: int
                           ) -> TreeNode:
    if end_index < start_index:
        return None

    middle_index = (start_index + end_index) // 2

    bst = TreeNode(array_sub[middle_index])

    bst.left = construct_balanced_bst(array_sub,
                                      start_index,
                                      middle_index - 1)
    bst.right = construct_balanced_bst(array_sub,
                                       middle_index + 1,
                                       end_index)

    return bst
