# ---Permutations---

from typing import List


def get_permutations(array: List[int]) -> List[List[int]]:
    permutations = list()
    permutations_helper(array, [], permutations)
    return permutations


def permutations_helper(
        array: List[int], perm: List[int], perms: List[List[int]]
):
    if not len(array) and len(perm):
        perms.append(perm)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]
            new_perm = perm + [array[i]]
            permutations_helper(new_array, new_perm, perms)


print(get_permutations([1, 2, 3]))
