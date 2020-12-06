# ---Group Anagrams---

from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    return_list = list()
    used_words = dict()

    for i in range(len(words)):
        current_word = words[i]
        anagrams_list = [current_word]

        if words[i] in used_words.keys():
            continue

        for r in range(len(words)):
            if i == r:
                continue

            if are_anagrams(words[i], words[r]):
                anagrams_list.append(words[r])
                used_words[words[r]] = 0

        return_list.append(anagrams_list)

    return return_list


def are_anagrams(word1: str, word2: str):
    return sorted(word1) == sorted(word2)


words_input = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
output = list(map(lambda x: sorted(x), group_anagrams(words_input)))

print(output)
# [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
