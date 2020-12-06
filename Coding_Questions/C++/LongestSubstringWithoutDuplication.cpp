// ---Longest Substring Without Duplication---

#include <map>
#include <vector>
#include <algorithm>


std::string longest_substring_without_duplication(std::string str) {
    std::map<char, size_t> last_seen;
    std::vector<size_t> indices = {0, 1};
    size_t start_index = 0;

    for (size_t i = 0; i < str.length(); ++i) {
        if (last_seen.find(str[i]) != last_seen.cend()) {
            start_index = std::max(start_index, last_seen[str[i]] + 1);
        }
        if (indices[1] - indices[0] < i + 1 - start_index) {
            indices = {start_index, i + 1};
        }
        last_seen[str[i]] = i;
    }

    return str.substr(indices[0], indices[1] - indices[0]);
}