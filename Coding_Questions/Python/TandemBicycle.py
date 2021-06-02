from typing import List


def tandem_bicycle(
        red_shirt_speeds: List[int],
        blue_shirt_speeds: List[int],
        fastest: bool
) -> int:
    red_shirt_speeds.sort(reverse=fastest)
    blue_shirt_speeds.sort()

    print(red_shirt_speeds)
    print(blue_shirt_speeds)

    total_speed = 0
    for i in range(len(red_shirt_speeds)):
        total_speed += red_shirt_speeds[i] if red_shirt_speeds[i] > \
        blue_shirt_speeds[i] else blue_shirt_speeds[i]

    return total_speed


r_speeds = [5, 5, 3, 9, 2]
b_speeds = [3, 6, 7, 2, 1]
fastest_bool = False
output = tandem_bicycle(r_speeds, b_speeds, fastest_bool)
print(f"{output} == 25")
assert output == 25
