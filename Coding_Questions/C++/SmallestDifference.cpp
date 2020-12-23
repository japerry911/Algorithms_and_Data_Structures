// ---Smallest Difference---

#include <vector>


int calculate_difference(int num1, int num2) {
    return abs(num1 - num2);
}


std::vector<int> smallest_difference(std::vector<int> array1, std::vector<int> array2) {
    std::sort(array1.begin(), array1.end());
    std::sort(array2.begin(), array2.end());

    int pointer1 = 0;
    int pointer2 = 0;

    std::pair<std::vector<int>, int> current_smallest_pair = {{}, INT_MAX};

    while (pointer1 < array1.size() && pointer2 < array2.size()) {
        int pair_difference = calculate_difference(array1[pointer1], array2[pointer2]);

        if (pair_difference == 0) {
            return {array1[pointer1], array2[pointer2]};
        }

        if (pair_difference < current_smallest_pair.second) {
            current_smallest_pair = {{array1[pointer1], array2[pointer2]}, pair_difference};
        }

        if (array1[pointer1] < array2[pointer2]) {
            ++pointer1;
        } else {
            ++pointer2;
        }
    }

    return current_smallest_pair.first;
}


