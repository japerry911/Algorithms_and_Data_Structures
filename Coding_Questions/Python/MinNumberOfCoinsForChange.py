from typing import List

import pytest


def min_number_of_coins_for_change(n: int, denoms: List) -> int:
    """how many coins to produce n, smallest number of coins, and use denoms

    :param int n: produce this amount of change
    :param denoms: use these as coin options
    :rtype: int
    :returns: smallest number of coins needed to make change
    """
    pass


def test_min_number_of_coins_for_change():
    denoms_test = [1, 5, 10]
    n_test = 7
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 3

    denoms_test = [1, 10, 5]
    n_test = 7
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 3

    denoms_test = [10, 1, 5]
    n_test = 7
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 3

    denoms_test = [1, 2, 3]
    n_test = 0
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 0

    denoms_test = [2, 1]
    n_test = 3
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 2

    denoms_test = [39, 45, 130, 40, 4, 1]
    n_test = 135
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 3

    denoms_test = [1, 3, 4]
    n_test = 10
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 3

    denoms_test = [2, 4]
    n_test = 7
    print(f"min({n_test}, {denoms_test}) == 3")
    result = min_number_of_coins_for_change(n_test, denoms_test)
    assert result == 7


pytest.main(["MinNumberOfCoinsForChange.py"])
