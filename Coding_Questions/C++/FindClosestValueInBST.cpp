// ---Find Closest Value in BST---


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


int find_closest_value_in_bst(BST *tree, int target) {
    int closest_value = (target >= 0 ? INT_MAX : INT_MIN);
    BST *current_node = tree;

    while (current_node != nullptr) {
        int proposed_closest_value_distance = abs(current_node->value - target);

        if (proposed_closest_value_distance == 0) {
            return current_node->value;
        }

        if (proposed_closest_value_distance < abs(closest_value - target)) {
            closest_value = current_node->value;
        }

        if (target < current_node->value) {
            current_node = current_node->left;
        } else {
            current_node = current_node->right;
        }
    }

    return closest_value;
}