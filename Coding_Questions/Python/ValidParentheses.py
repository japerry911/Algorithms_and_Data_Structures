import pytest


def is_valid(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{', '}',
        '[' and ']', determine if the input string is valid
    :param str s: the actual string being validated
    :returns: True or False for whether it is valid or not
    :rtype: bool
    """
    if not len(s):
        return False
    elif len(s) % 2 == 1:
        return False
    elif s[0] == ")" or s[0] == "]" or s[0] == "}":
        return False

    stack = list()

    for idx, char in enumerate(s):
        if char == "{" or char == "[" or char == "(":
            stack.append(char)
        elif (char == "}" or char == "]" or char == ")") and not len(stack):
            return False
        elif char == "}" and stack[-1] == "{":
            stack.pop()
        elif char == "]" and stack[-1] == "[":
            stack.pop()
        elif char == ")" and stack[-1] == "(":
            stack.pop()
        else:
            return False

    return len(stack) == 0


def test_is_valid():
    print("is_valid(()) == True")
    assert is_valid("()") is True

    print("is_valid(()[]{}) == True")
    assert is_valid("()[]{}") is True

    print("is_valid((]) == False")
    assert is_valid("(]") is False

    print("is_valid(([)]) == False")
    assert is_valid("([)]") is False

    print("is_valid({[]}) == True")
    assert is_valid("{[]}") is True


pytest.main(["ValidParentheses.py"])
