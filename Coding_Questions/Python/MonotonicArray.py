from typing import List

import pytest


def is_monotonic(array: List[int]) -> bool:
    pass


def test_is_monotonic():
    input_1 = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    expected_output = True
    assert is_monotonic(input_1) == expected_output

    input_2 = list()
    expected_output = True
    assert is_monotonic(input_2) == expected_output

    input_3 = [1]
    expected_output = True
    assert is_monotonic(input_3) == expected_output

    input_4 = [1, 2]
    expected_output = True
    assert is_monotonic(input_4) == expected_output

    input_5 = [2, 1]
    expected_output = True
    assert is_monotonic(input_5) == expected_output

    input_6 = [1, 5, 10, 1100, 1101, 1102, 9001]
    expected_output = True
    assert is_monotonic(input_6) == expected_output

    input_7 = [-1, -5, -10, -1100, -1101, -1102, -9001]
    expected_output = True
    assert is_monotonic(input_7) == expected_output

    input_8 = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
    expected_output = False
    assert is_monotonic(input_8) == expected_output


pytest.main(["MonotonicArray"])
