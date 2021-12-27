from typing import List

import pytest


def has_single_cycle(array: List[int]) -> bool:
    """Checks if a everything has been hopped on at only once

    :param List[int] array: input list of integers
    :rtype: bool
    :returns: true or false, whether it did a have a single cycle or not
    """
    num_elements_visited = 0
    current_idx = 0

    while num_elements_visited < len(array):
        if num_elements_visited > 0 and current_idx == 0:
            return False
        num_elements_visited += 1
        current_idx = get_next_idx(current_idx, array)

    return current_idx == 0


def get_next_idx(current_idx: int, array: List[int])  -> int:
    jmp = array[current_idx]
    next_idx = (current_idx + jmp) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


def test_has_single_cycle():
    input_test = [2, 3, 1, -4, -4, 2]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [2, 2, -1]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [2, 2, 2]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [1, 1, 1, 1, 1]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [-1, 2, 2]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [0, 1, 1, 1, 1]
    expected_output = False
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [10, 11, -6, -23, -2, 3, 88, 909, -26]
    expected_output = False
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output

    input_test = [1, 2, 3, 4, -2, 3, 7, 8, -26]
    expected_output = True
    output = has_single_cycle(input_test)
    print(f"{output} == {expected_output}")
    assert output == expected_output


pytest.main(["SingleCycleCheck.py"])
