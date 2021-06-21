import pytest


def str_str(haystack: str, needle: str) -> int:
    pass


def test_str_str():
    print("haystack(hello, ll) == 2")
    assert str_str("hello", "ll") == 2

    print("haystack(aaaaaa, bba) == -1")
    assert str_str("aaaaaa", "bba") == -1

    print("haystack(,) == 0")
    assert str_str("", "") == 0


pytest.main(["StrStr.py"])
