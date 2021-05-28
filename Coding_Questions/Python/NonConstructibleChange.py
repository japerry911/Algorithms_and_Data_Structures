from typing import List


def non_constructible_change(coins: List[int]) -> int:
    coins_sorted = sorted(coins)


a = non_constructible_change([5, 7, 1, 1, 2, 3, 22])
print(a)
assert a == 20
