# ---Find Closest Value in BST---
import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_value_in_bst(tree: BST, target: int) -> int:
    current_node = tree
    closest_value = math.inf

    while current_node is not None:
        current_closeness = abs(closest_value - target)
        proposed_closeness = abs(current_node.value - target)

        if proposed_closeness <= current_closeness:
            closest_value = current_node.value
            if closest_value == target:
                return closest_value

        if target < current_node.value:
            current_node = current_node.left
        else:
            current_node = current_node.right

    return closest_value


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print(find_closest_value_in_bst(root, 12))  # 13
