# ---Underscorify Substring---

from typing import List


def underscorify_substring(string: str, substring: str) -> str:
    locations_list = build_locations_2d_list(string, substring)
    collapsed_locations_list = collapse_locations_list(locations_list)
    return build_underscore_string(collapsed_locations_list, string)


def build_underscore_string(locations_list: List[List[int]], string: str) -> str:
    underscores = 0
    for sub_list in locations_list:
        string = string[:sub_list[0] + underscores] + "_" + \
                 string[sub_list[0] +
                        underscores:sub_list[1] + 1 + underscores] + "_" + \
                 string[sub_list[1] + 1 + underscores:]
        underscores += 2
    return string


def collapse_locations_list(locations_list: List[List[int]]) \
        -> List[List[int]]:
    collapsed_list = list()
    previous_sub_list = None
    idx = -1

    for sub_list in locations_list:
        if previous_sub_list is None:
            collapsed_list.append(sub_list)
            idx += 1
        elif previous_sub_list[1] + 1 != \
                sub_list[0]:
            collapsed_list.append(sub_list)
            idx += 1
        else:
            collapsed_list[idx][1] = sub_list[1]

        previous_sub_list = sub_list

    return collapsed_list


def build_locations_2d_list(string: str, substring: str) -> List[List[int]]:
    locations_list = list()
    sub_idx = 0
    start_idx = 0
    previous = None

    for idx, character in enumerate(string):
        if previous == substring[sub_idx]:
            previous = None
            sub_idx += 1
            if sub_idx < len(substring) and character == substring[sub_idx]:
                sub_idx += 1
                if sub_idx == len(substring):
                    locations_list.append([start_idx, idx])
                    start_idx = idx + 1
                    sub_idx = 0
                    previous = character
                continue
            else:
                sub_idx -= 1

        if character == substring[sub_idx]:
            sub_idx += 1
            if sub_idx == len(substring):
                locations_list.append([start_idx, idx])
                start_idx = idx + 1
                sub_idx = 0
                previous = character
        else:
            sub_idx = 0
            start_idx = idx + 1
            previous = None

    return locations_list


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

assert actual == expected
assert actual2 == expected2
