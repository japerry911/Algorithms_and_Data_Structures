// ---Branch Sums---

#include <vector>


class BinaryTree {
public:
    int value;
    BinaryTree *left;
    BinaryTree *right;

    BinaryTree(int value) {
        this->value = value;
        left = NULL;
        right = NULL;
    }
};


void calc_branch_sums(BinaryTree *node, int current_sum, std::vector<int> &running_sums) {
    if (node->left != nullptr) {
        calc_branch_sums(node->left, current_sum + node->left->value, running_sums);
    }

    if (node->right != nullptr) {
        calc_branch_sums(node->right, current_sum + node->right->value, running_sums);
    }

    if (node->left == nullptr && node->right == nullptr) {
        running_sums.push_back(current_sum);
    }
}


std::vector<int>branch_sums(BinaryTree *root) {
    std::vector<int> running_sums;
    calc_branch_sums(root, root->value, running_sums);
    return running_sums;
}