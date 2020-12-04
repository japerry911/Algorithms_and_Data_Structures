// ---Validate BST---


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


bool validate_bst_helper(BST *tree, int min_value, int max_value) {
    return (min_value <= tree->value  && tree->value < max_value);
}


bool validate_bst(BST *tree, int min_value=INT_MIN, int max_value=INT_MAX) {
    if (!validate_bst_helper(tree, min_value, max_value)) {
        return false;
    }

    if (tree->left != nullptr) {
        if (!validate_bst(tree->left, min_value, tree->value)) {
            return false;
        }
    }

    if (tree->right != nullptr) {
        if (!validate_bst(tree->right, tree->value, max_value)) {
            return false;
        }
    }

    return true;
}