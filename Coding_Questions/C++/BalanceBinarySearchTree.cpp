// --- Balance Binary Search Tree---

#include <vector>
#include <math.h>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};



void in_order_traverse(TreeNode* tree, std::vector<int> &vector) {
    if (tree != nullptr) {
        in_order_traverse(tree->left, vector);
        vector.push_back(tree->val);
        in_order_traverse(tree->right, vector);
    }
}

TreeNode* construct_balanced_BST(const std::vector<int> &in_order_vector,
        int start_index, int end_index) {
    if (end_index < start_index) {
        return nullptr;
    }

    size_t middle_index = floor((end_index + start_index) / 2);
    int middle_value = in_order_vector[middle_index];

    TreeNode* bst = new TreeNode(middle_value);

    bst->left = construct_balanced_BST(in_order_vector, start_index, middle_index - 1);
    bst->right = construct_balanced_BST(in_order_vector, middle_index + 1, end_index);

    return bst;
}


TreeNode* balance_BST(TreeNode* root) {
    std::vector<int> in_order_vector = {};
    in_order_traverse(root, in_order_vector);
    return construct_balanced_BST(in_order_vector, 0, in_order_vector.size() - 1);
}