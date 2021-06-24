import pytest


def add_binary(a: str, b: str) -> str:
    result = ""
    current_idx_a = -1
    current_idx_b = -1
    carry_over = 0

    while abs(current_idx_a) <= len(a) or abs(current_idx_b) <= len(b):
        current_value = carry_over
        if abs(current_idx_a) <= len(a):
            current_value += int(a[current_idx_a])
        if abs(current_idx_b) <= len(b):
            current_value += int(b[current_idx_b])

        if current_value == 0:
            carry_over = 0
            result = "0" + result
        elif current_value == 1:
            carry_over = 0
            result = "1" + result
        elif current_value == 2:
            carry_over = 1
            result = "0" + result
        elif current_value == 3:
            carry_over = 1
            result = "1" + result

        current_idx_a -= 1
        current_idx_b -= 1

    if carry_over == 1:
        result = "1" + result

    return result


def test_add_binary():
    print("add_binary(11, 1) == 100")
    assert add_binary("11", "1") == "100"

    print("add_binary(1010, 1011) == 10101")
    assert add_binary("1010", "1011") == "10101"

    print("add_binary(111, 111) == 1110")
    assert add_binary("111", "111") == "1110"

    print("add_binary(0, 0) == 0")
    assert add_binary("0", "0") == "0"


pytest.main(["AddBinary.py"])
