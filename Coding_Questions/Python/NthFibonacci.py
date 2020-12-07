# ---Nth Fibonacci---

from typing import Dict

# Solution 1: O(2^n) Time | O(n) Space
# def get_nth_fib(n: int) -> int:
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return get_nth_fib(n - 1) + get_nth_fib(n - 2)


# Solution 2: O(n) Time | O(n) Space
# def get_nth_fib(n: int, memoize: Dict[int, int] = None) -> int:
#     if memoize is None:
#         memoize = {1: 0, 2: 1}
#
#     if n in memoize.keys():
#         return memoize[n]
#     else:
#         memoize[n] = get_nth_fib(n - 1, memoize) + get_nth_fib(n - 2, memoize)
#         return memoize[n]


# Solution 3: O(n) Time | O(1) Space
def get_nth_fib(n: int) -> int:
    fibonacci_numbers_pair = [0, 1]

    for _ in range(2, n):
        fibonacci_number = fibonacci_numbers_pair[0] + \
                           fibonacci_numbers_pair[1]
        fibonacci_numbers_pair = [
            fibonacci_numbers_pair[1],
            fibonacci_number
            ]

    return fibonacci_numbers_pair[1] if n > 1 else fibonacci_numbers_pair[0]


print(get_nth_fib(6))  # 5
print(get_nth_fib(13))  # 144
print(get_nth_fib(21))  # 6765
