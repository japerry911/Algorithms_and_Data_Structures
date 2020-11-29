//
// Created by John Perry on 11/29/20.
//

#include <vector>
#include <map>

// Solution 1: O(n^2) Time | O(1) Space
//std::vector<int> two_number_sum(std::vector<int> array, int target_sum) {
//    for (int i = 0; i < array.size(); ++i) {
//        for (int c = 0; c < array.size(); ++c) {
//            if (i == c) {
//                continue;
//            } else if (array[i] + array[c] == target_sum) {
//                return std::vector<int> {array[i], array[c]};
//            }
//        }
//    }
//    return {};
//}


// Solution 2: O(n) Time | O(n) Space
//std::vector<int> two_number_sum(std::vector<int> array, int target_sum) {
//    std::map<int, bool> nums;
//    for (const auto num : array) {
//        int possible_match = target_sum - num;
//        if (nums.count(possible_match) == 1) {
//            return std::vector<int> {num, possible_match};
//        } else {
//            nums[num] = true;
//        }
//    }
//    return {};
//}


// Solution 3: O(nlog(n)) Time | O(1) Space
std::vector<int> two_number_sum(std::vector<int> array, int target_sum) {
    std::sort(array.begin(), array.end());
    int left = 0;
    int right = array.size() - 1;
    while (left < right) {
        int possible_match = array[left] + array[right];
        if (possible_match == target_sum) {
            return std::vector<int> {array[left], array[right]};
        } else if (possible_match < target_sum) {
            ++left;
        } else if (possible_match > target_sum) {
            --right;
        }
    }
    return {};
}