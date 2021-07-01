from typing import List

import pytest


def move_element_to_end(array: List[int], to_move: int) -> List[int]:
    """Moves all instances of to_move to the end of list, and returns list,
        ***order does not need to be maintained for integers as long as to_move
        is at the end
    :param List[int] array: input numbers List
    :param int to_move: the integer to move to the end of the List
    :returns: returns list of numbers with to_move instances at the end
    :rtype: List[int]
    """
    farthest_idx = len(array) - 1
    idx = 0

    while idx < farthest_idx:
        if array[idx] == to_move:
            array[idx] = array[farthest_idx]
            array[farthest_idx] = to_move
            farthest_idx -= 1
        else:
            idx += 1

    return array


def test_move_element_to_end():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    expected = [4, 1, 3, 2, 2, 2, 2, 2]
    assert move_element_to_end(array, to_move) == expected

    array = []
    to_move = 3
    expected = []
    assert move_element_to_end(array, to_move) == expected

    array = [1, 2, 4, 5, 6]
    to_move = 3
    expected = [1, 2, 4, 5, 6]
    assert move_element_to_end(array, to_move) == expected


pytest.main(["MoveElementToEnd.py"])
