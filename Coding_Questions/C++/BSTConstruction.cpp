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


    BST &remove(int val) {
        return *this;
    }
};