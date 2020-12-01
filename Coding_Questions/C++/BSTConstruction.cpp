// ---BST Construction---

#include <vector>


class BST {
public:
    int value;
    BST *left;
    BST *right;


    BST(int val) {
        value = val;
        left = NULL;
        right = NULL;
    }


    BST &insert(int val) {
        return *this;
    }


    bool contains(int val) {
        return false;
    }


    BST &remove(int val) {
        return *this;
    }
};