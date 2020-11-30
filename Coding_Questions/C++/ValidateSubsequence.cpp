// ---Validate Subsequences---

#include <vector>


// Solution 1: O(n) Time | O(1) Space
bool is_valid_subsequence(std::vector<int> array, std::vector<int> sequence) {
    int arr_index = 0;
    int seq_index = 0;
    while (arr_index < array.size() && seq_index < sequence.size()) {
        if (array[arr_index] == sequence[seq_index]) {
            ++seq_index;
        }
        ++arr_index;
    }
    return seq_index == sequence.size();
}