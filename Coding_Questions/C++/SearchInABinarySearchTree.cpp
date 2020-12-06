// ---Search in a Binary Search Tree---


class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* current_node = root;
        
        while (current_node != nullptr) {
            if (val > current_node->val) {
                current_node = current_node->right;
            } else if (val < current_node->val) {
                current_node = current_node->left;
            } else {
                return current_node;
            }
        }
        
        return nullptr;
    }
};