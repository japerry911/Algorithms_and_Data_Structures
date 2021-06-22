import pytest


def length_of_last_word(s: str) -> int:
    try:
        return len(list(filter(lambda ss: ss != "", s.split()))[-1])
    except IndexError:
        return 0


def test_length_of_last_word():
    print("length_of_last_word(Hello World) == 5")
    assert length_of_last_word("Hello World") == 5

    print("length_of_last_word() == 0")
    assert length_of_last_word(" ") == 0

    print("length_of_last_word( a) == 1")
    assert length_of_last_word(" a") == 1


pytest.main(["LengthOfLastWord"])
