from typing import List

import pytest


def longest_peak(array: List[int]) -> int:
    """takes in an array of integers, and determines the longest peak, a peak
        is when an array is strictly increase for at least 3 values and then
        decreases
    :param List[int] array: the input array of integers
    :returns: the length of the longest peak
    :rtype: int
    """
    pass


def test_longest_peak():
    input_1 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    expected_output_1 = 6
    assert longest_peak(input_1) == expected_output_1

    input_2 = list()
    expected_output_2 = 0
    assert longest_peak(input_2) == expected_output_2

    input_3 = [1, 3, 2]
    expected_output_3 = 3
    assert longest_peak(input_3) == expected_output_3

    input_4 = [1, 2, 3, 4, 5, 1]
    expected_output_4 = 6
    assert longest_peak(input_4) == expected_output_4

    input_5 = [5, 4, 3, 2, 1, 2, 1]
    expected_output_5 = 3
    assert longest_peak(input_5) == expected_output_5

    input_6 = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
    expected_output_6 = 5
    assert longest_peak(input_6) == expected_output_6

    input_7 = [5, 4, 3, 2, 1, 2, 10, 12]
    expected_output_7 = 0
    assert longest_peak(input_7) == expected_output_7


pytest.main(["LongestPeak"])
