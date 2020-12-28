class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(self, root: TreeNode) -> bool:
    if root is None:
        return True
    else:
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        current_status = abs(left - right) <= 1

        return current_status and self.isBalanced(
            root.left) and self.isBalanced(root.right)


def max_depth(self, root: TreeNode) -> int:
    return 0 if root is None else max(self.max_depth(root.left),
                                      self.max_depth(root.right)) + 1