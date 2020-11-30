#include <iostream>
#include <vector>
#include "TwoNumberSum.cpp"
#include "ValidateSubsequence.cpp"


int main() {
//    const auto answer = two_number_sum(std::vector<int> {3, 5, -4, 8, 11, 1, -1, 6}, 10);
//    for (const auto i : answer) {
//        std::cout << i << ", ";
//    }

    const auto answer = is_valid_subsequence(std::vector<int> {5, 1, 22, 25, 6, -1, 8, 10}, {1, 6, -1, 10});
    std::cout << std::boolalpha << answer<< std::endl;

    return 0;
}