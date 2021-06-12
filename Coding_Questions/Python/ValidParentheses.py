import pytest


def is_valid(s: str) -> bool:
    pass


def test_is_valid():
    print("is_valid(()) == True")
    assert is_valid("()") is True

    print("is_valid(()[]{}) == True")
    assert is_valid("()[]{}") is True

    print("is_valid((]) == False")
    assert is_valid("(]") is False

    print("is_valid(([)]) == False")
    assert is_valid("([)]") is False

    print("is_valid({[]}) == True")
    assert is_valid("{[]}") is True


pytest.main(["ValidParentheses.py"])
