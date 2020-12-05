// ---BST Traversal---

#include <vector>


class BST {
public:
    int value;
    BST *left;
    BST *right;


    explicit BST(int val) {
        value = val;
        left = nullptr;
        right = nullptr;
    }
};


void in_order_traverse(BST *tree, std::vector<int> &array) {
    if (tree != nullptr) {
        in_order_traverse(tree->left, array);
        array.push_back(tree->value);
        in_order_traverse(tree->right, array);
    }
}


void pre_order_traverse(BST *tree, std::vector<int> &array) {
    if (tree != nullptr) {
        array.push_back(tree->value);
        pre_order_traverse(tree->left, array);
        pre_order_traverse(tree->right, array);
    }
}


void post_order_traverse(BST *tree, std::vector<int> &array) {
    if (tree != nullptr) {
        post_order_traverse(tree->left, array);
        post_order_traverse(tree->right, array);
        array.push_back(tree->value);
    }
}
