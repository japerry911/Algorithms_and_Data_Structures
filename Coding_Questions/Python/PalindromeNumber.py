import pytest


def is_palindrome(x: int) -> bool:
    """Determines whether an inputted integer is a Palindrome number of not
    :param int x: the number being tested
    :returns: True or False indicating if it is Palindromic
    :rtype: bool
    """
    if x < 0:
        return False
    elif 0 < x < 10:
        return True

    number = x
    reverse = 0

    while number > 0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number //= 10

    return reverse == x


def test_is_palindrome():
    print("is_palindrome(121) is True")
    assert is_palindrome(121) is True

    print("is_palindrome(-121) is False")
    assert is_palindrome(-121) is False

    print("is_palindrome(10) is False")
    assert is_palindrome(10) is False

    print("is_palindrome(-101) is False")
    assert is_palindrome(-101) is False

    print("is_palindrome(3) is True")
    assert is_palindrome(3) is True

    print("is_palindrome(9339) is True")
    assert is_palindrome(9339) is True


pytest.main(["PalindromeNumber.py"])
