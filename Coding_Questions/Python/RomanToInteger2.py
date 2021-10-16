import pytest


def roman_to_int(s: str) -> int:
    """Converts roman numeral to integer

    :param str s: inputted roman numeral
    :returns: converted integer value
    :rtype: int
    """
    look_up_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1_000
    }

    converted_integers = [look_up_dict[c] for c in s]

    running_total = 0
    i = 0
    while i < len(converted_integers):
        current_integer = converted_integers[i]

        if i + 1 < len(converted_integers):
            next_value = converted_integers[i + 1]

            if current_integer >= next_value:
                running_total += current_integer
                i += 1
            else:
                running_total += next_value - current_integer
                i += 2
        else:
            running_total += current_integer
            i += 1

    return running_total


def test_roman_to_int():
    print("roman_to_int(\"III\") == 3")
    assert roman_to_int("III") == 3

    print("roman_to_int(\"IV\") == 4")
    assert roman_to_int("IV") == 4

    print("roman_to_int(\"IX\") == 9")
    assert roman_to_int("IX") == 9

    print("roman_to_int(\"LVIII\") == 58")
    assert roman_to_int("LVIII") == 58

    print("roman_to_int\"MCMXCIV == 1994")
    assert roman_to_int("MCMXCIV") == 1994


pytest.main(["RomanToInteger2.py"])
