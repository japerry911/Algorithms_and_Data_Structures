// ---Bubble Sort---

#include <vector>


std::vector<int> bubble_sort(std::vector<int> array) {
    int counter = 0;
    for (;;) {
        bool swapped_occurred = false;

        for (int i = 0; i < array.size() - 1 - counter; ++i) {
            if (array[i] > array[i + 1]) {
                std::swap(array[i], array[i + 1]);
                swapped_occurred = true;
            }
        }

        if (!swapped_occurred) {
            break;
        }

        ++counter;
    }

    return array;
}