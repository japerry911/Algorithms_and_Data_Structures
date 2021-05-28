from typing import List


def non_constructible_change(coins: List[int]) -> int:
    coins.sort()
    change = 0

    for coin in coins:
        if change + 1 < coin:
            return change + 1
        else:
            change += coin

    return change + 1


# [1, 1, 2, 3, 5, 7, 22]
a = non_constructible_change([5, 7, 1, 1, 2, 3, 22])
print(f"{a} == 20")
assert a == 20
