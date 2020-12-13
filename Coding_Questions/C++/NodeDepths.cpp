// ---Node Depths---


class BinaryTree {
  public:
  int value;
  BinaryTree *left;
  BinaryTree *right;

  BinaryTree(int value) {
    this->value = value;
    left = nullptr;
    right = nullptr;
  }
};


int node_depths(BinaryTree *root, int depth=0) {
  return (depth + 
    (root->left == nullptr ? 0 : node_depths(root->left, depth + 1)) +
    (root->right == nullptr ? 0 : node_depths(root->right, depth + 1)));
}