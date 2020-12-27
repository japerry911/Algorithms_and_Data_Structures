// ---Underscorify Substring---

#include <vector>


std::vector<std::vector<int>> get_locations(const std::string &str, const std::string &substring) {
    std::vector<std::vector<int>> locations_2d_vector;
    int current_idx = 0;

    while (current_idx < str.size()) {
        int spot_idx = str.find(substring, current_idx);
        if (spot_idx != std::string::npos) {
            locations_2d_vector.push_back({spot_idx, spot_idx + (int)substring.size()});
            current_idx = spot_idx + 1;
        } else {
            break;
        }
    }

    return locations_2d_vector;
}


std::vector<std::vector<int>> collapse_vector(const std::vector<std::vector<int>> &vec) {
    std::vector<std::vector<int>> collapsed_vector;
    bool first_run = true;

    for (const auto &location_vec : vec) {
        if (first_run) {
            collapsed_vector.push_back(location_vec);
            first_run = false;
        } else {
            if (collapsed_vector[collapsed_vector.size() - 1][1] >= location_vec[0]) {
                collapsed_vector[collapsed_vector.size() - 1][1] = location_vec[1];
            } else {
                collapsed_vector.push_back(location_vec);
            }
        }
    }

    return collapsed_vector;
}


std::string underscorify(const std::string &str, const std::vector<std::vector<int>> &locations_vec) {
    std::string return_str = str;
    int underscores_added = 0;

    for (const auto &location_vec : locations_vec) {
        return_str = return_str.substr(0, location_vec[0] + underscores_added) + "_" +
                return_str.substr(location_vec[0] + underscores_added, location_vec[1] - location_vec[0]) +
                "_" + return_str.substr(location_vec[1] + underscores_added);
        underscores_added += 2;
    }

    return return_str;
}


std::string underscorify_substring(const std::string &str, const std::string &substring) {
    std::vector<std::vector<int>> locations_2d_vec = get_locations(str, substring);
    std::vector<std::vector<int>> collapsed_locations_2d_vec = collapse_vector(locations_2d_vec);
    std::string return_str = underscorify(str, collapsed_locations_2d_vec);
    return return_str;
}