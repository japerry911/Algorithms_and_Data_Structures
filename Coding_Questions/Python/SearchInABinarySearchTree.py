# ---Search in a Binary Search Tree--


def searchBST(root: TreeNode, val: int) -> TreeNode:
    current_node = root

    while current_node is not None:
        if val > current_node.val:
            current_node = current_node.right
        elif val < current_node.val:
            current_node = current_node.left
        else:
            return current_node

    return None
