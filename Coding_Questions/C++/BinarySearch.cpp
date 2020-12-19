// ---Binary Search---

#include <vector>
#include "math.h"


int binary_search_helper(std::vector<int> array, int target, int lower_pointer, int right_pointer) {
    while (lower_pointer <= right_pointer) {
        int middle_point = floor((lower_pointer + right_pointer) / 2);
        if (array[middle_point] == target) {
            return middle_point;
        } else if (array[middle_point] > target) {
            right_pointer = middle_point - 1;
        } else if (array[middle_point] < target) {
            lower_pointer = middle_point + 1;
        }
    }
    return -1;
}


int binary_search(std::vector<int> array, int target) {
    return binary_search_helper(array, target, 0, array.size());
}


