class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """checks to see if both input Binary Trees are the same
    :param TreeNode p: input Binary Tree
    :param TreeNode q: input Binary Tree
    :returns: returns boolean saying whether they are the same trees or not
    :rtype: bool
    """
    if p is None or q is None:
        return p == q

    if p.val != q.val:
        return False

    if is_same_tree(p.left, q.left) is False:
        return False

    if is_same_tree(p.right, q.right) is False:
        return False

    return True
