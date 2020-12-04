# ---Palindrome Check---


def is_palindrome(string: str) -> bool:
    return string.lower() == "".join(reversed(list(string))).lower()


print(is_palindrome("abcdcba"))  # True
