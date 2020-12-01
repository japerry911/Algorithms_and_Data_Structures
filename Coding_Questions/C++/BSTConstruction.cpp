// ---BST Construction---

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


    BST &insert(int val) {
        BST *current_node = this;

        for (;;) {
            if (val < current_node->value) {
                if (current_node->left == nullptr) {
                    current_node->left = new BST(val);
                    break;
                } else {
                    current_node = current_node->left;
                }
            } else {
                if (current_node->right == nullptr) {
                    current_node->right = new BST(val);
                    break;
                } else {
                    current_node = current_node->right;
                }
            }
        }

        return *this;
    }


    bool contains(int val) {
        BST *current_node = this;

        while (current_node != nullptr) {
            if (val < current_node->value) {
                current_node = current_node->left;
            } else if (val > current_node->value) {
                current_node = current_node->right;
            } else {
                return true;
            }
        }

        return false;
    }


    BST &remove(int val, BST *parent_node=nullptr) {
        BST *current_node = this;

        while (current_node != nullptr) {
            if (val < current_node->value) {
                parent_node = current_node;
                current_node = current_node->left;
            } else if (value > current_node->value) {
                parent_node = current_node;
                current_node = current_node->right;
            } else {
                if (current_node->left != nullptr && current_node->right != nullptr) {
                    // current_node->value => smallest value of right subtree
                    current_node->value = current_node->right->get_min_value();
                    current_node->right->remove(current_node->value, current_node);
                } else if (parent_node == nullptr) {
                    if (current_node->left != nullptr) {
                        current_node->value = current_node->left->value;
                        current_node->right = current_node->left->right;
                        current_node->left = current_node->left->left;
                    } else if (current_node->right != nullptr) {
                        current_node->value = current_node->right->value;
                        current_node->left = current_node->right->left;
                        current_node->right = current_node->right->right;
                    }
                } else if (parent_node->left == current_node) {
                    parent_node->left = (current_node->left != nullptr ? current_node->left : current_node->right);
                } else if (parent_node->right == current_node) {
                    current_node->right = (current_node->left != nullptr ? current_node->left : current_node->right);
                }
                break;
            }
        }

        return *this;
    }


    int get_min_value() {
        BST *current_node = this;
        while (current_node->left != nullptr) {
            current_node = current_node->left;
        }
        return current_node->value;
    }
};