// ---Count Number of Consistent Strings---


#include <vector>


int count_consistent_strings(std::string allowed, std::vector<std::string> &words) {
    int consistent_strings = words.size();

    for (const auto &word : words) {
        for (const auto &character : word) {
            if (word.find(character) == std::string::npos) {
                --consistent_strings;
                break;
            }
        }
    }

    return consistent_strings;
}