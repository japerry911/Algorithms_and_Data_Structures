# ---Count Number of Consistent Strings---

from typing import List


def count_consistent_strings(allowed: str, words: List[str]) -> int:
    consistent_strings = len(words)

    for word in words:
        for character in word:
            if character not in allowed:
                consistent_strings -= 1
                break

    return consistent_strings


# def count_consistent_strings(allowed: str, words: List[str]) -> int:
#     non_consistent_strings = 0
#
#     for word in words:
#         is_consistent = True
#
#         for character in word:
#             if character not in allowed:
#                 non_consistent_strings += 1
#                 break
#
#     return len(words) - non_consistent_strings


# def count_consistent_strings(allowed: str, words: List[str]) -> int:
#     consistent_strings = 0
#
#     for word in words:
#         is_consistent = True
#
#         for character in word:
#             if character not in allowed:
#                 is_consistent = False
#                 break
#
#         if is_consistent is True:
#             consistent_strings += 1
#
#     return consistent_strings


# def count_consistent_strings(allowed: str, words: List[str]) -> int:
#     consistent_strings = 0
#
#     for word in words:
#         not_allowed_characters = list(filter(
#             lambda character: character not in allowed,
#             word
#         ))
#
#         consistent_strings += 1 if len(not_allowed_characters) == 0 else 0
#
#     return consistent_strings


words1 = ["ad", "bd", "aaab", "baa", "badab"]
allowed1 = "ab"
actual = count_consistent_strings(allowed1, words1)
expected = 2
print(actual)  # 2
assert actual == expected
