import pytest


def add_binary(a: str, b: str) -> str:
    pass


def test_add_binary():
    print("add_binary(11, 1) == 100")
    assert add_binary("11", "1") == "100"

    print("add_binary(1010, 1011) == 10101")
    assert add_binary("1010", "1011") == "10101"


pytest.main(["AddBinary.py"])
