from typing import List, Tuple

import pytest


def is_monotonic(array: List[int]) -> bool:
    """evaluates a List and tells if it is monotonic or not
    :param List[int] array: input list that is being evaluated
    :returns: True or False, which tells if input is monotonic or not
    :rtype: bool
    """
    def find_second_element(
            input_array: List[int],
            prev: int
    ) -> Tuple[int, List[int]]:
        return_element = input_array.pop(0)
        if return_element == prev:
            return find_second_element(input_array, prev)
        return return_element, input_array

    if len(array) <= 2:
        return True

    first_element = array.pop(0)

    try:
        second_element, array = find_second_element(array, first_element)
    except IndexError:
        return True

    is_increasing = first_element < second_element
    current_element = second_element

    for element in array:
        if (is_increasing and current_element > element) or \
                (not is_increasing and current_element < element):
            return False
        current_element = element

    return True


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

    input_9 = [1, 2, 0]
    expected_output = False
    assert is_monotonic(input_9) == expected_output

    input_10 = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
    expected_output = False
    assert is_monotonic(input_10) == expected_output

    input_11 = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
    expected_output = True
    assert is_monotonic(input_11) == expected_output

    input_12 = [-1, -1, -1, -1, -1, -1, -1, -1]
    expected_output = True
    assert is_monotonic(input_12) == expected_output


pytest.main(["MonotonicArray"])
