// ---Powerset---

#include <vector>


std::vector<std::vector<int>> powerset(std::vector<int> array) {
    std::vector<std::vector<int>> subsets = {{}};

    for (const auto element : array) {
        int subsets_length = subsets.size();
        for (int i = 0; i < subsets_length; ++i) {
            std::vector<int> new_element = subsets[i];
            new_element.push_back(element);
            subsets.push_back(new_element);
        }
    }

    return subsets;
}