// ---Group Anagrams---

#include <vector>
#include <map>


bool are_anagrams(std::string word1, std::string word2) {
    std::sort(word1.begin(), word1.end());
    std::sort(word2.begin(), word2.end());
    return word1 == word2;
}


std::vector<std::vector<std::string>> group_anagrams(std::vector<std::string> words) {
    std::vector<std::vector<std::string>> return_vector;
    std::map<std::string, size_t> words_map;

    for (size_t i = 0; i < words.size(); ++i) {
        std::vector<std::string> current_vector = {words[i]};
        if (words_map.find(words[i]) != words_map.cend()) {
            continue;
        }
        for (size_t r = 0; r < words.size(); ++r) {
            if (r == i) {
                continue;
            }

            if (are_anagrams(words[i], words[r]) && words_map.find(words[r]) == words_map.cend()) {
                current_vector.push_back(words[r]);
                words_map[words[r]] = 0;
            }
        }
        return_vector.push_back(current_vector);
    }

    return return_vector;
}