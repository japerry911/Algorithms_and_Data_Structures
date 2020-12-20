// ---Insertion Sort---

#include <vector>


std::vector<int> insertion_sort(std::vector<int> array) {
    for (int i = 1; i < array.size(); ++i) {
        int counter = 0;
        for (int j = i - 1; j >= 0; --j) {
            if (array[i - counter] < array[j]) {
                std::swap(array[i - counter], array[j]);
                ++counter;
            } else {
                break;
            }
        }
    }

    return array;
}
