// ---Spiral Traverse---

#include <vector>


std::vector<int> spiral_traverse(std::vector<std::vector<int>> array) {
    int start_row = 0;
    int start_column = 0;
    int end_row = array.size() - 1;
    int end_column = array[0].size() - 1;

    std::vector<int> return_vector;

    while (start_row <= end_row && start_column <= end_column) {
        for (int c = start_column; c <= end_column; ++c) {
            return_vector.push_back(array[start_row][c]);
        }

        for (int r = start_row + 1; r <= end_row; ++r) {
            return_vector.push_back(array[r][end_column]);
        }

        for (int c = end_column - 1; c >= start_column; --c) {
            if (start_row == end_row) {
                break;
            }
            return_vector.push_back(array[end_row][c]);
        }

        for (int r = end_row - 1; r > start_row; --r) {
            if (start_column == end_column) {
                break;
            }
            return_vector.push_back(array[r][start_column]);
        }

        ++start_row;
        ++start_column;
        --end_row;
        --end_column;
    }

    return return_vector;
}