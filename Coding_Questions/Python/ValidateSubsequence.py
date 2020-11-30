from typing import List


# ---Validate Subsequence---


# Solution 1: O(n) Time | O(1) Space
# def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
#     in_sequence_check = False
#     seq_index = 0
#     for num in array:
#         if seq_index == len(sequence):
#             return True
#         if in_sequence_check is False and num == sequence[seq_index]:
#             seq_index += 1
#             in_sequence_check = True
#             continue
#         if num == sequence[seq_index]:
#             seq_index += 1
#         elif num in sequence:
#             seq_index = 0
#             in_sequence_check = False
#     return seq_index == len(sequence)


# Solution 2: O(n) Time | O(1) Space
def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(sequence):
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(sequence)


print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10],
                           [25]))
