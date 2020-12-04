# ---ValidateBST---

import math


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


# Solution 1
def validate_bst(tree: BST,
                 min_value: int = -math.inf,
                 max_value: int = math.inf
                 ) -> bool:
    if validate_bst_helper(tree, min_value, max_value) is False:
        return False

    if tree.left is not None:
        if validate_bst(tree.left, min_value, tree.value) is False:
            return False
    if tree.right is not None:
        if validate_bst(tree.right, tree.value, max_value) is False:
            return False

    return True


def validate_bst_helper(tree: BST,
                        min_value: int = -math.inf,
                        max_value: int = math.inf 
                        ) -> bool:
    return min_value <= tree.value < max_value


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print(validate_bst(root))  # True
