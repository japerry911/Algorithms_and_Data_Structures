import pytest


def reverse_words_in_string(string: str) -> str:
    """Reverses words in a string

    :param str string: input string to be reversed
    :rtype: str
    :returns: reversed string
    """
    pass


def test_reverse_words_in_string():
    string_test = "AlgoExpert is the best!"
    expected_result = "best! the is AlgoExpert"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "Reverse These Words"
    expected_result = "Words These Reverse"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "..H,, hello 678"
    expected_result = "678 hello ..H,,"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "1 12 23 34 56"
    expected_result = "56 34 23 12 1"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "this-is-one-word"
    expected_result = "this-is-one-word"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = ""
    expected_result = ""
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "words, separated, by, commas"
    expected_result = "commas by, separated, words,"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "this      string     has a     lot of   whitespace"
    expected_result = "whitespace   of lot     a has     string      this"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result

    string_test = "test        "
    expected_result = "        test"
    print(f"{string_test} == {expected_result}")
    assert reverse_words_in_string(string_test) == expected_result


pytest.main(["ReverseWordsInString.py"])
