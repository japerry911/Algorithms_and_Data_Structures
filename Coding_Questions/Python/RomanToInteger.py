import pytest


def roman_to_int(s: str) -> int:
    pass


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
