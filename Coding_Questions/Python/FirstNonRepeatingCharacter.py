# ---First Non-Repeating Character---

def first_non_repeating_character(string: str) -> int:
    for idx, char in enumerate(string):
        count = string.count(char)
        if count == 1:
            return idx

    return -1


a = first_non_repeating_character("abcdcaf")
assert a == 1
