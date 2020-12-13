# ---Branch Sums---

from typing import List


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def branch_sums(root: BinaryTree) -> int:
    sums = list()
    calc_branch_sums(root, root.value, sums)
    return sums


def calc_branch_sums(node: BinaryTree,
                     current_sum: int,
                     running_sums: List[int]):
    if node.left is not None:
        calc_branch_sums(node.left,
                         current_sum + node.left.value,
                         running_sums)

    if node.right is not None:
        calc_branch_sums(node.right,
                         current_sum + node.right.value,
                         running_sums)

    if node.left is None and node.right is None:
        running_sums.append(current_sum)


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
print(branch_sums(tree))  # [15, 16, 18, 10, 11]
