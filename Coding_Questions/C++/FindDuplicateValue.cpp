// ---Find Duplicate Value---

#include <vector>
#include <set>


int find_duplicate_value(std::vector<int> array) {
    std::set<int> holding_set;

    for (const auto &element : array) {
        if (holding_set.find(element) != holding_set.cend()) {
            return element;
        }
        holding_set.insert(element);
    }

    return -1;
}