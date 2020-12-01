#include <iostream>
#include <vector>
#include "TwoNumberSum.cpp"
#include "ValidateSubsequence.cpp"
#include "BSTConstruction.cpp"


int main() {
//    Two Number Sum
//    const auto answer = two_number_sum(std::vector<int> {3, 5, -4, 8, 11, 1, -1, 6}, 10);
//    for (const auto i : answer) {
//        std::cout << i << ", ";
//    }

//    Validate Subsequence
//    const auto answer = is_valid_subsequence(std::vector<int> {5, 1, 22, 25, 6, -1, 8, 10}, {1, 6, -1, 10});
//    std::cout << std::boolalpha << answer<< std::endl;

//    BST Construction
    BST *root = new BST(10);
    root->left = new BST(5);
    root->left->left = new BST(2);
    root->left->left->left = new BST(1);
    root->left->right = new BST(5);
    root->right = new BST(15);
    root->right->left = new BST(13);
    root->right->left->right = new BST(14);
    root->right->right = new BST(22);

    root->insert(12);

    std::cout << root->right->left->left->value << std::endl; // 12
    std::cout << std::boolalpha << root->contains(15) << std::endl; // true

    return 0;
}