# ---BST Construction---

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Solution 2:
    #   Average: O(log(n)) Time | O(1) Space
    #   Worst: O(n) Time | O(1) Space
    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = BST(value)
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = BST(value)
                    break
        return self

    # Solution 1
    #   Average: O(log(n)) Time | O(n) Space
    #   Worst: O(n) Time | O(n) Space
    # def insert(self, value):
    #     if value < self.value:
    #         if self.left is not None:
    #             self.left.insert(value)
    #         else:
    #             self.left = BST(value)
    #     else:
    #         if self.right is not None:
    #             self.right.insert(value)
    #         else:
    #             self.right = BST(value)
    #
    #     return self

    #   Average: O(log(n)) Time | O(1) Space
    #   Worst: O(n) Time | O(1) Space
    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    # Average: O(log(n)) Time | O(1) Space
    # Worst: O(n) Time | O(1) Space
    def remove(self, value, parent_node=None):
        current_node = self
        while current_node is not None:
            # value is less than the current node's value look left
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            # value is greater than the current node's value, look right
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            # found node to remove
            else:
                # check if it has to children nodes
                if current_node.left is not None and current_node.right is \
                        not None:
                    # smallest value of right subtree
                    current_node.value = current_node.right.get_min_value()
                    # remove the smallest value of right subtree since it is
                    #   replacing the original node that we are removing
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # This is a single node tree, do nothing
                        pass
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left \
                        is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if \
                        current_node.left is not None else current_node.right
                break
        return self

    # find min value by keep going to the left till you can't anymore, then
    #   return the value of the selected node
    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


"""
                        10
                       /  \
                      5    15
                     / \   / \
                    2   5 13  22
                   /        \
                  1          14
          
"""
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

root.insert(12)
print(root.contains(12))  # True
print(root.contains(10))  # True
print(root.contains(30))  # False


root.remove(10)
print(root.contains(10))
print(root.value)
