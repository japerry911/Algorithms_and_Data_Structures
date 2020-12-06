# ---Longest Palindromic Substring---


def longest_palindromic_substring(string: str) -> str:
    longest_palindrome = "a"

    for i in range(len(string)):
        for r in range(i + 1, len(string)):
            if is_palindromic(string[i:r + 1]) and len(string[i:r + 1]) > len(
                    longest_palindrome
            ):
                longest_palindrome = string[i: r + 1]

    return longest_palindrome


def is_palindromic(string: str) -> bool:
    return string == "".join(reversed(list(string)))


print(longest_palindromic_substring("abaxyzzyxf"))  # "xyzzyx"
assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"
