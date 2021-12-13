def minimum_characters_for_words(words):
    # Write your code here.
    max_frequencies_dict = dict()

    for word in words:
        word_frequencies_dict = dict()
        for char in word:
            if char not in word_frequencies_dict:
                word_frequencies_dict[char] = 1
            else:
                word_frequencies_dict[char] += 1

        for k, v in word_frequencies_dict.items():
            if k not in max_frequencies_dict:
                max_frequencies_dict[k] = v
            else:
                max_frequencies_dict[k] = max(max_frequencies_dict[k], v)

    char_list = list()
    for k, v in max_frequencies_dict.items():
        for _ in range(v):
            char_list.append(k)

    return char_list
