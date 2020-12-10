// ---Min Height BST---

#include <vector>
#include <cmath>


class BST {
public:
    int value;
    BST *left;
    BST *right;

    explicit BST(int value) {
        this->value = value;
        left = nullptr;
        right = nullptr;
    }

    void insert(int val) {
        BST *current_node = this;

        for (;;) {
            if (value < current_node->value) {
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
    }
};


BST *construct_min_height_bst(std::vector<int> array_sub, int start_index, int end_index) {
    if (end_index < start_index) {
        return nullptr;
    }

    int middle_index = floor((end_index - start_index) / 2);

    BST *bst = new BST(array_sub[middle_index]);

    bst->left = construct_min_height_bst(array_sub, start_index, middle_index - 1);
    bst->right = construct_min_height_bst(array_sub, middle_index + 1, end_index);

    return bst;
}


BST *min_height_bst(const std::vector<int> &array) {
    return construct_min_height_bst(array, 0, array.size() - 1);
}