// ---Selection Sort---

#include <vector>


std::vector<int> selection_sort(std::vector<int> array) {
    for (int i = 0; i < array.size(); ++i) {
        int pointer = i;
        for (int c = i + 1; c < array.size(); ++c) {
            if (array[pointer] > array[c]) {
                pointer = c;
            }
        }
        std::swap(array[i], array[pointer]);
    }
    return array;
}
