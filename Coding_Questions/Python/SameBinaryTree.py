class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None or q is None:
        return p == q

    if p.val != q.val:
        return False

    if is_same_tree(p.left, q.left) is False:
        return False

    if is_same_tree(p.right, q.right) is False:
        return False

    return True
