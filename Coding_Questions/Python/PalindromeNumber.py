import pytest


def is_palindrome(x: int) -> bool:
    """Determines whether an inputted integer is a Palindrome number of not
    :param int x: the number being tested
    :returns: True or False indicating if it is Palindromic
    :rtype: bool
    """
    return False


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
