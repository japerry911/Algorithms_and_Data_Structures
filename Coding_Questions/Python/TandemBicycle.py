from typing import List


def tandem_bicycle(
        red_shirt_speeds: List[int],
        blue_shirt_speeds: List[int],
        fastest: bool
) -> int:
    combined = sorted(red_shirt_speeds + blue_shirt_speeds)
    return sum(combined[len(red_shirt_speeds):]) if fastest is True else \
        sum(combined[:len(red_shirt_speeds)])


r_speeds = [5, 5, 3, 9, 2]
b_speeds = [3, 6, 7, 2, 1]
fastest_bool = True
output = tandem_bicycle(r_speeds, b_speeds, fastest_bool)
print(f"{output} == 32")
assert output == 32
