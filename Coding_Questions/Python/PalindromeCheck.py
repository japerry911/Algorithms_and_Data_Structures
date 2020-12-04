# ---Palindrome Check---


def is_palindrome(string: str) -> bool:
    return string == "".join(reversed(list(string)))


print(is_palindrome("abcdcba"))  # True
