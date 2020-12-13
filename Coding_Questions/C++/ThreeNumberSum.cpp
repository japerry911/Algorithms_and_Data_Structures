// ---Three Number Sum---

#include <vector>


std::vector<std::vector<int>> three_number_sum(std::vector<int> array, int target_sum) {
    std::vector<std::vector<int>> return_vector;
    std::sort(array.begin(), array.end());

    for (int i = 0; i < array.size(); ++i) {
        int left_pointer = i + 1;
        int right_pointer = array.size() - 1;

        while (left_pointer < right_pointer) {
            int current_sum = array[i] + array[left_pointer] + array[right_pointer];

            if (current_sum < target_sum) {
                ++left_pointer;
            } else if (current_sum > target_sum) {
                --right_pointer;
            } else {
                return_vector.push_back({array[i], array[left_pointer], array[right_pointer]});
                ++left_pointer;
                --right_pointer;
            }
        }
    }

    return return_vector;
}