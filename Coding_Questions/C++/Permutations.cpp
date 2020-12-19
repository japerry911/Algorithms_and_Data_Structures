// ---Permutations---

#include <vector>



void permutation_helper(int idx, std::vector<int> &array, std::vector<std::vector<int>> &perms) {
    if (idx == array.size() - 1) {
        perms.push_back(array);
    } else {
        for (size_t j = idx; j < array.size(); ++j) {
            std::swap(array[idx], array[j]);
            permutation_helper(idx + 1, array, perms);
            std::swap(array[idx], array[j]);
        }
    }
}


std::vector<std::vector<int>> get_permutations(std::vector<int> array) {
    std::vector<std::vector<int>> perms;
    permutation_helper(0, array, perms);
    return perms;
}
