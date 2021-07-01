from typing import List


def maximum_wealth(accounts: List[List[int]]) -> int:
    return max([sum(x) for x in accounts])
