import pytest
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    longest_prefix = ""
    current_idx = 0
    min_str_length = min(map(len, strs))

    while current_idx < min_str_length:
        for idx, string in enumerate(strs):
            if idx == 0:
                longest_prefix += string[current_idx]
            elif longest_prefix != string[:current_idx + 1]:
                return longest_prefix[:current_idx]

        current_idx += 1

    return longest_prefix[:current_idx]


def test_longest_common_prefix():
    print("longest_common_prefix([\"flower\", \"flow\", \"flight\"] = fl")
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    print("longest_common_prefix([\"dog\", \"racecar\", \"car\"]) = \"\")")
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


pytest.main(["LargestCommonPrefix.py"])
