class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    """Finds Max Depth of Binary Tree
    :param TreeNode root: the tree that is being calculated max depth
    :returns: the max depth
    :rtype: int
    """
    if root is None:
        return 0

    depth_left = 1 + max_depth(root.left)
    depth_right = 1 + max_depth(root.right)

    return max(depth_left, depth_right)
