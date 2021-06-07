import pytest


def roman_to_int(s: str) -> int:
    """Converts Roman Numeral to Integer
    :param str s: Roman Numeral input
    :returns: converted Integer
    :rtype: int
    """
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    converted_integer = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman_dict:
            converted_integer += roman_dict[s[i:i + 2]]
            i += 2
        else:
            converted_integer += roman_dict[s[i]]
            i += 1

    return converted_integer


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


pytest.main(["RomanToInteger.py"])
