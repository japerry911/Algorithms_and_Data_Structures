#include <iostream>
#include "TwoNumberSum.cpp"
#include <vector>


int main() {
    const auto answer = two_number_sum(std::vector<int> {3, 5, -4, 8, 11, 1, -1, 6}, 10);
    for (const auto i : answer) {
        std::cout << i << ", ";
    }

    return 0;
}