from typing import List


def count_matches(items: List[List[str]], rule_key: str, rule_value: str) \
        -> int:
    """counts anything that matches the rule, using the base rule keys list of
        ["type", "color", "name"]
    :param List[List[str]] items: the 2D list of items
    :param str rule_key: the rule_key being used to look up
    :param str rule_value: the rule_value being used to look up
    :returns: the count of times that the rules are triggered in the items list
    :rtype: int
    """
    keys_list = ["type", "color", "name"]
    look_at_idx = keys_list.index(rule_key)
    return len(list(filter(lambda x: x[look_at_idx] == rule_value, items)))
