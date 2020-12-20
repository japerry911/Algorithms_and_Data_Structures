// ---Find Three Largest Numbers---

#include <vector>


void update_and_shift(std::vector<int> &three_largest, const int &element, const int &idx) {
    for (int i = 0; i < idx; ++i) {
        three_largest[i] = three_largest[i + 1];
    }
    three_largest[idx] = element;
}


void update_largest(std::vector<int> &three_largest, const int &element) {
    if (three_largest[2] < element) {
        update_and_shift(three_largest, element, 2);
    } else if (three_largest[1] < element) {
        update_and_shift(three_largest, element, 1);
    } else if (three_largest[0] < element) {
        update_and_shift(three_largest, element, 0);
    }
}


std::vector<int> find_three_largest_numbers(const std::vector<int> &array) {
    std::vector<int> three_largest = {INT_MIN, INT_MIN, INT_MIN};
    for (const auto i : array) {
        update_largest(three_largest, i);
    }
    return three_largest;
}

