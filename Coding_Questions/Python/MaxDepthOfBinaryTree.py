# ---Max Depth of Binary Tree---

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(self, root: TreeNode, depth: int = 0) -> int:
    return 0 if root is None else max(self.maxDepth(root.left),
                                      self.maxDepth(root.right)) + 1
