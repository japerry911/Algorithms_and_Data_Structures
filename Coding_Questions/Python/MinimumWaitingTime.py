from itertools import permutations
import math
from typing import List


def minimum_waiting_time_helper(queries: List) -> int:
    total = 0
    for i in range(len(queries) - 1):
        total += queries[i]
        for r in range(i):
            total += queries[r]

    return total


def minimum_waiting_time(queries: List) -> int:
    perms = [list(x) for x in list(permutations(queries))]
    min_waiting_time = math.inf

    for perm in perms:
        waiting_time = minimum_waiting_time_helper(perm)

        if min_waiting_time > waiting_time:
            min_waiting_time = waiting_time

    return min_waiting_time


queries_input = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
expected_output = 17
output = minimum_waiting_time(queries_input)
print(f"output {output} == {expected_output}")
assert output == expected_output
