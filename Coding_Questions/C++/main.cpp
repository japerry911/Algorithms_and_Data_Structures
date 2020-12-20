#include <iostream>
#include <vector>
#include "TwoNumberSum.cpp"
#include "ValidateSubsequence.cpp"
//#include "BSTConstruction.cpp"
//#include "FindClosestValueInBST.cpp"
//#include "ValidateBST.cpp"
#include "CheckPalindrome.cpp"
#include "CaesarCipherEncryptor.cpp"
//#include "BSTTraversal.cpp"
#include "RunLengthEncoding.cpp"
#include "LongestPalindromicSubstring.cpp"
#include "GroupAnagrams.cpp"
#include "LongestSubstringWithoutDuplication.cpp"
#include "NthFibonacci.cpp"
#include "MinHeightBST.cpp"
#include "BalanceBinarySearchTree.cpp"
#include "SpiralTraverse.cpp"
#include "ThreeNumberSum.cpp"
#include "Permutations.cpp"
#include "DepthFirstSearch.cpp"
#include "BinarySearch.cpp"
#include "FindThreeLargestNumbers.cpp"


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
//    BST *root = new BST(10);
//    root->left = new BST(5);
//    root->left->left = new BST(2);
//    root->left->left->left = new BST(1);
//    root->left->right = new BST(5);
//    root->right = new BST(15);
//    root->right->left = new BST(13);
//    root->right->left->right = new BST(14);
//    root->right->right = new BST(22);
//
//    root->insert(12);
//
//    std::cout << root->right->left->left->value << std::endl; // 12
//
//    root->remove(10);
//
//    std::cout << std::boolalpha << root->contains(10) << std::endl; // false
//    std::cout << std::boolalpha << root->contains(15) << std::endl; // true

//    BST *root = new BST(10);
//    root->left = new BST(5);
//    root->left->left = new BST(2);
//    root->left->left->left = new BST(1);
//    root->left->right = new BST(5);
//    root->right = new BST(15);
//    root->right->left = new BST(13);
//    root->right->left->right = new BST(14);
//    root->right->right = new BST(22);
//
//    int actual = find_closest_value_in_bst(root, 12);
//
//    std::cout << actual << std::endl; // 13

//    BST *root = new BST(10);
//    root->left = new BST(5);
//    root->left->left = new BST(2);
//    root->left->left->left = new BST(1);
//    root->left->right = new BST(5);
//    root->right = new BST(15);
//    root->right->left = new BST(13);
//    root->right->left->right = new BST(14);
//    root->right->right = new BST(22);
//
//    bool actual = validate_bst(root);
//
//    std::cout << std::boolalpha << actual << std::endl; // true

//    bool actual = is_palindrome("abcdcba");
//
//    std::cout << std::boolalpha << actual << std::endl; // true

//    std::string actual = caesar_cypher_encryptor("abc", 57);
//
//    std::cout << actual << std::endl; // "fgh"

//    std::string actual = run_length_encoding("AAAAAAAAAAAAABBCCCCDD");
//    std::cout << actual << std::endl;
//    assert(actual == "9A4A2B4C2D");
//    std::string actual2 = run_length_encoding("aA");
//    assert(actual2 == "1a1A");

//    std::string actual = longest_palindromic_substring("abaxyzzyxf");
//    std::cout << actual << std::endl;
//    assert(actual == "xyzzyx");

//    std::vector<std::vector<std::string>> actual = group_anagrams({"yo",  "act", "flop", "tac",
//                                                                   "foo", "cat", "oy",   "olfp"});
//    for (const auto &i : actual) {
//        for (const auto &r : i) {
//            std::cout << r << ", ";
//        }
//        std::cout << std::endl;
//    }

//    std::string actual = longest_substring_without_duplication("clementisacap");
//    std::cout << actual << std::endl;
//    assert(actual == "mentisac");

//    int actual = get_nth_fib(6);
//    std::cout << actual << std::endl; // 5

//    std::vector<std::vector<int>> perms = get_permutations({1, 2, 3});
//
//    for (const auto i : perms) {
//        for (const auto j : i) {
//            std::cout << j << " , ";
//        }
//        std::cout << std::endl;
//    }

    std::vector<int> input1 = {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};
    std::vector<int> actual1 = find_three_largest_numbers(input1);
    for (const auto i : actual1) {
        std::cout << i << ", ";
    }
    std::cout << std::endl;

    return 0;
}