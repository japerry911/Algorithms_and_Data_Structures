from typing import List


def class_photos(
        red_shirt_heights: List[int],
        blue_shirt_heights: List[int]
) -> bool:
    red_shirt_heights.sort()
    blue_shirt_heights.sort()

    zipped_list = list(zip(red_shirt_heights, blue_shirt_heights))

    print(zipped_list)

    rows_set = False
    first_row_red = None
    for red_shirt, blue_shirt in zipped_list:
        if rows_set is False:
            if red_shirt < blue_shirt:
                first_row_red = True
            elif red_shirt > blue_shirt:
                first_row_red = False
            else:
                return False
            rows_set = True
        else:
            if first_row_red is True:
                if red_shirt >= blue_shirt:
                    return False
            else:
                if red_shirt <= blue_shirt:
                    return False

    return True


red = [19, 19, 21, 1, 1, 1, 1, 1]
blue = [20, 5, 4, 4, 4, 4, 4, 4]
output = class_photos(red, blue)
assert not output
