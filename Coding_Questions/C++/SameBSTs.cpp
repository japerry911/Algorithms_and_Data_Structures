// ---Same BSTs---

#include <vector>


std::vector<int> left_values_gatherer(std::vector<int> array) {
    int compare_value = array[0];
    std::vector<int> return_vec;

    for (int i = 1; i < array.size(); ++i) {
        if (array[i] < compare_value) {
            return_vec.push_back(array[i]);
        }
    }

    return return_vec;
}


std::vector<int> right_values_gatherer(std::vector<int> array) {
    int compare_value = array[0];
    std::vector<int> return_vec;

    for (int i = 1; i < array.size(); ++i) {
        if (array[i] >= compare_value) {
            return_vec.push_back(array[i]);
        }
    }

    return return_vec;
}


bool same_bsts(std::vector<int> array1, std::vector<int> array2) {
    if (array1.empty() || array2.empty()) {
        return true;
    } else if (array1.size() != array2.size() || array1[0] != array2[0]) {
        return false;
    }

    std::vector<int> left_subtree_values1 = left_values_gatherer(array1);
    std::vector<int> left_subtree_values2 = left_values_gatherer(array2);
    std::vector<int> right_subtree_values1 = right_values_gatherer(array1);
    std::vector<int> right_subtree_values2 = right_values_gatherer(array2);

    return same_bsts(left_subtree_values1, left_subtree_values2) &&
           same_bsts(right_subtree_values1, right_subtree_values2);
}
