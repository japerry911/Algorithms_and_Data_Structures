from typing import List

import pytest


def array_of_products(array: List[int]) -> List[int]:
    pass


def test_array_of_products():
    input_1 = [5, 1, 4, 2]
    expected_output_1 = [8, 40, 10, 20]
    assert array_of_products(input_1) == expected_output_1

    input_2 = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert array_of_products(input_2) == expected_output_2

    input_3 = [-1, -1, -1]
    expected_output_3 = [1, 1, 1]
    assert array_of_products(input_3) == expected_output_3

    input_4 = [4, 4]
    expected_output_4 = [4, 4]
    assert array_of_products(input_4) == expected_output_4


pytest.main(["ArrayOfProducts"])
