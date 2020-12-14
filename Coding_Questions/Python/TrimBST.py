# ---Trim BST---


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
    if root is None:
        return None
    elif low <= root.val <= high:
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
    elif low > root.val:
        return self.trimBST(root.right, low, high)
    else:
        # must be high < root.val
        return self.trimBST(root.left, low, high)