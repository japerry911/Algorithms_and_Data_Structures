// ---Max Subset Sum No Adjacent---

#include <vector>


int max_subset_sum_no_adjacent(std::vector<int> array) {
    if (array.empty()) {
        return 0;
    }

    for (int i = 2; i < array.size(); ++i) {
        array[i] += *std::max_element(array.cbegin(), array.cend() - array.size() + i - 1);
    }

    return *std::max_element(array.cbegin(), array.cend());
}