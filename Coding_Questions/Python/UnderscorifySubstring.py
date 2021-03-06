# ---Underscorify Substring---

from typing import List


# -----------------Solution 2--------------------------------------
def underscorify_substring(string: str, substring: str) -> str:
    locations_list = get_locations(string, substring)
    collapsed_locations_list = collapse_locations(locations_list)
    string = underscorify(collapsed_locations_list, string)
    return string


def underscorify(collapsed_locations_list: List[List[int]], string: str) \
        -> str:
    underscores_added = 0
    for locations_sub_list in collapsed_locations_list:
        string = string[:locations_sub_list[0] + underscores_added] + "_" + \
                 string[locations_sub_list[0] +
                        underscores_added:locations_sub_list[1] +
                                          underscores_added] + \
                 "_" + string[locations_sub_list[1] + underscores_added:]
        underscores_added += 2

    return string


def get_locations(input_string: str, input_substring: str) -> List[List[int]]:
    locations_list = list()
    current_idx = 0

    while current_idx < len(input_string):
        spot_idx = input_string.find(input_substring, current_idx)
        if spot_idx != -1:
            locations_list.append([spot_idx, spot_idx + len(input_substring)])
            current_idx = spot_idx + 1
        else:
            break

    return locations_list


def collapse_locations(locations_list: List[List[int]]) -> List[List[int]]:
    collapsed_locations_list = list()
    first_time = True

    for location_sub_list in locations_list:
        if first_time is True:
            collapsed_locations_list.append(location_sub_list)
            first_time = False
        else:
            if collapsed_locations_list[
                len(collapsed_locations_list) - 1
            ][1] >= location_sub_list[0]:
                collapsed_locations_list[
                    len(collapsed_locations_list) - 1
                ][1] = location_sub_list[1]
            else:
                collapsed_locations_list.append(location_sub_list)

    return collapsed_locations_list

# -----------------Solution 2--------------------------------------
# def underscorify_substring(string: str, substring: str) -> str:
#     locations_list = build_locations_2d_list(string, substring)
#     collapsed_locations_list = collapse_locations_list(locations_list)
#     return build_underscore_string(collapsed_locations_list, string)
#
#
# def build_underscore_string(locations_list: List[List[int]], string: str) -> str:
#     underscores = 0
#     for sub_list in locations_list:
#         string = string[:sub_list[0] + underscores] + "_" + \
#                  string[sub_list[0] +
#                         underscores:sub_list[1] + underscores] + "_" + \
#                  string[sub_list[1] + underscores:]
#         underscores += 2
#     return string
#
#
# def collapse_locations_list(locations: List[List[int]]) \
#         -> List[List[int]]:
#     if not len(locations):
#         return locations
#     new_locations = [locations[0]]
#     previous = new_locations[0]
#     for i in range(1, len(locations)):
#         current = locations[i]
#         if current[0] <= previous[1]:
#             previous[1] = current[1]
#         else:
#             new_locations.append(current)
#             previous = current
#     return new_locations
#
#
# def build_locations_2d_list(string: str, substring: str) -> List[List[int]]:
#     locations = list()
#     start_idx = 0
#     while start_idx < len(string):
#         next_idx = string.find(substring, start_idx)
#         if next_idx != -1:
#             locations.append([next_idx, next_idx + len(substring)])
#             start_idx = next_idx + 1
#         else:
#             break
#     return locations


actual = underscorify_substring(
    "abababababababababababababaababaaabbababaa", "a"
)
expected = "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b" \
           "_aaa_bb_a_b_a_b_aa_"
print(f"EXPECTED:\t{expected}")
print("------------------------")
print(f"ACTUAL:\t\t{actual}")
actual2 = underscorify_substring(
    "testthis is a testtest to see if testestest it works", "test"
)
expected2 = "_test_this is a _testtest_ to see if _testestest_ it works"
print(f"EXPECTED:\t{expected2}")
print("------------------------")
print(f"ACTUAL:\t\t{actual2}")
actual3 = underscorify_substring(
    "ttttttttttttttbtttttctatawtatttttastvb", "ttt"
)
expected3 = "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb"
print(f"EXPECTED:\t{expected3}")
print("------------------------")
print(f"ACTUAL:\t\t{actual3}")
assert actual == expected
assert actual2 == expected2
assert actual3 == expected3
