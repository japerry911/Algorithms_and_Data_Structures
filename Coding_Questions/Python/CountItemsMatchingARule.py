from typing import List


def count_matches(items: List[List[str]], rule_key: str, rule_value: str) \
        -> int:
    keys_list = ["type", "color", "name"]
    look_at_idx = keys_list.index(rule_key)
    return len(list(filter(lambda x: x[look_at_idx] == rule_value, items)))
