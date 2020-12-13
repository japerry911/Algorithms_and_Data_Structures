# ---Node Depths---


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def node_depths(root: BinaryTree, depth: int = 0) -> int:
    return depth + \
           (0 if root.left is None else node_depths(root.left, depth + 1)) + \
           (0 if root.right is None else node_depths(root.right, depth + 1))


root_test = BinaryTree(1)
root_test.left = BinaryTree(2)
root_test.left.left = BinaryTree(4)
root_test.left.left.left = BinaryTree(8)
root_test.left.left.right = BinaryTree(9)
root_test.left.right = BinaryTree(5)
root_test.right = BinaryTree(3)
root_test.right.left = BinaryTree(6)
root_test.right.right = BinaryTree(7)
actual = node_depths(root_test)
print(actual)  # 16
assert actual == 16
