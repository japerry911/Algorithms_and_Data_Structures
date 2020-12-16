# ---Invert Binary Tree---


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree.left is not None and tree.right is not None:
        right = tree.right
        tree.right = tree.left
        tree.left = right
    elif tree.left is None and tree.right is not None:
        tree.left = tree.right
        tree.right = None
    elif tree.left is not None and tree.right is None:
        tree.right = tree.left
        tree.left = None
    else:
        return tree

    if tree.left is not None:
        tree.left = invert_binary_tree(tree.left)

    if tree.right is not None:
        tree.right = invert_binary_tree(tree.right)

    return tree
