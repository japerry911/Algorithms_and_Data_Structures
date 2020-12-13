# ---Delete Node in a BST---


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def delete_node(self, root: TreeNode, key: int, parent_node: TreeNode = None) \
            -> TreeNode:
        if root is None:
            return None

        whole_tree = root
        current_node = root

        while current_node is not None:
            if key < current_node.val:
                parent_node = current_node
                current_node = current_node.left
            elif key > current_node.val:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is \
                        not None:
                    # get the smallest val from right subtree and set to current
                    #   node
                    current_node.val = self.get_min_val(current_node.right)
                    # remove the smallest val that we just found in right subtree
                    #   since we just used it to replace the removed node val
                    self.delete_node(current_node.right,
                                               current_node.val,
                                               current_node)
                # is the current node the root node
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.val = current_node.left.val
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.val = current_node.right.val
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                # is current_node a left child or right child
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is \
                        not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is \
                        not None else current_node.right
                else:
                    parent_node = current_node
                break

        if current_node is not None and parent_node is not None:
            return parent_node
        elif parent_node is None and (current_node.left is not None or
                                      current_node.right is not None):
            return current_node
        elif parent_node is None and current_node.left is None and \
                current_node.right is None:
            return list()
        else:
            return whole_tree

    @staticmethod
    def get_min_val(tree: TreeNode) -> int:
        current_node = tree
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.val


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(7)

a = Solution()
b = a.delete_node(root, 5)
print(b.val)
print(b.left.val)

