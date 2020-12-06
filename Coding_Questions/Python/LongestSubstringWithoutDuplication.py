# ---Longest Substring Without Duplication---


# Solution 1
# def longest_substring_without_duplication(string: str) -> str:
#     max_length = 1
#     long_string = string[0]
#     i = None
#
#     for r in range(len(string) - 1):
#         length = 1
#         char_dict = {string[r]: r}
#         break_early = 0
#         for i in range (r + 1, len(string)):
#             if string[i] in char_dict.keys():
#                 break_early = 1
#                 break
#
#             length += 1
#             char_dict[string[i]] = i
#
#         if length > max_length:
#             max_length = length
#             long_string = string[
#                           char_dict[string[r]]:
#                           char_dict[string[i - break_early]] + 1
#                           ]
#
#     return long_string


# Solution 2: O(n) Time | O(min(n, a)) Space
def longest_substring_without_duplication(string: str) -> str:
    last_seen = dict()
    longest = [0, 1]
    start_index = 0
    for i, char in enumerate(string):
        if char in last_seen:
            start_index = max(start_index, last_seen[char] + 1)
        if longest[1] - longest[0] < i + 1 - start_index:
            longest = [start_index, i + 1]
        last_seen[char] = i

    return string[longest[0]:longest[1]]


actual = longest_substring_without_duplication("clementisacap")
print(actual)  # "mentisac"
assert actual == "mentisac"

actual2 = longest_substring_without_duplication("abcbde")
print(actual2)  # "cbde"
assert actual2 == "cbde"

