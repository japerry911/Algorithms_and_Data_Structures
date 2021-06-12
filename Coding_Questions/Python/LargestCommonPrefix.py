import pytest
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    pass


def test_longest_common_prefix():
    print("longest_common_prefix([\"flower\", \"flow\", \"flight\"] = fl")
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    print("longest_common_prefix([\"dog\", \"racecar\", \"car\"]) = \"\")")
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


pytest.main(["LargestCommonPrefix.py"])
