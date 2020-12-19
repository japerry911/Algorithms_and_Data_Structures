# ---Permutations---

from typing import List


# Solution 2: O(n * n!) Time | O(n * n!) Space
# def get_permutations(array: List[int]) -> List[List[int]]:
#     perms = list()
#     permutations_helper(0, array, perms)
#     return perms
#
#
# def permutations_helper(idx: int, arr: List[int], perms: List[List[int]]):
#     if idx == len(arr) - 1:
#         perms.append(arr.copy())
#     else:
#         for j in range(idx, len(arr)):
#             swap(arr, idx, j)
#             permutations_helper(idx + 1, arr, perms)
#             swap(arr, idx, j)
#
#
# def swap(swap_arr: List[int], i: int, j: int):
#     swap_arr[i], swap_arr[j] = swap_arr[j], swap_arr[i]

from typing import Dict, List


def permutations(string: str) -> List[str]:
    perms = dict()
    permutations_helper(0, list(string), perms)
    return perms.keys()


def permutations_helper(idx: int, string: List[str], perms: Dict[str, int]):
    if idx == len(string) - 1:
        if "".join(string.copy()) not in perms:
            perms["".join(string.copy())] = 1
    else:
        for j in range(idx, len(string)):
            swap(string, idx, j)
            permutations_helper(idx + 1, string, perms)
            swap(string, idx, j)


def swap(string: List[str], i: int, j: int):
    string[i], string[j] = string[j], string[i]


# Solution 1: O(n^2 * n!) Time | O(n * n!) space
# def get_permutations(array: List[int]) -> List[List[int]]:
#     permutations = list()
#     permutations_helper(array, [], permutations)
#     return permutations
#
#
# def permutations_helper(
#         array: List[int], perm: List[int], perms: List[List[int]]
# ):
#     if not len(array) and len(perm):
#         perms.append(perm)
#     else:
#         for i in range(len(array)):
#             new_array = array[:i] + array[i + 1:]
#             new_perm = perm + [array[i]]
#             permutations_helper(new_array, new_perm, perms)


# print(get_permutations([1, 2, 3]))
print(permutations("aabb"))