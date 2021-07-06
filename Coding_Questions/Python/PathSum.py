class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, target_sum: int, current_sum: int = 0) -> \
        bool:
    """Calculates if there a a root-to-leaf path sum for the tree and
        target_sum
    :param TreeNode root: the tree that is being looked through
    :param int target_sum: the target_sum that needs to be calculated in path
        sum
    :param int current_sum: the current running sum of path, defaults to 0
    :returns: returns whether a path_sum is calculate-able
    :rtype: bool
    """
    if root is None:
        return False
    else:
        current_sum += root.val

    if current_sum == target_sum and root.left is None and root.right is None:
        return True

    return has_path_sum(root.left, target_sum, current_sum) | \
           has_path_sum(root.right, target_sum, current_sum)
