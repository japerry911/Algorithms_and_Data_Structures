from typing import List

import pytest


def move_element_to_end(array: List[int], to_move: int) -> List[int]:
    pass


def test_move_element_to_end():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    expected = [1, 3, 4, 2, 2, 2, 2, 2]
    assert move_element_to_end(array, to_move) == expected

    array = []
    to_move = 3
    expected = []
    assert move_element_to_end(array, to_move) == expected

    array = [1, 2, 4, 5, 6],
    to_move = 3
    expected = [1, 2, 4, 5, 6]
    assert move_element_to_end(array, to_move) == expected

pytest.main(["MoveElementToEnd.py"])
