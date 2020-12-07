// ---Nth Fibonacci---

#include <map>
#include <vector>


// Solution 1: O(2^n) Time | O(n) Space
//int get_nth_fib(int n) {
//    if (n == 1) {
//        return 0;
//    } else if (n == 2) {
//        return 1;
//    } else {
//        return get_nth_fib(n - 1) + get_nth_fib(n - 2);
//    }
//}


// Solution 2: O(n) Time | O(n) Space
//int get_nth_fib(int n, std::map<int, int> memoize={{1, 0}, {2, 1}}) {
//    if (memoize.find(n) != memoize.cend()) {
//        return memoize[n];
//    } else {
//        memoize[n] = get_nth_fib(n - 1, memoize) + get_nth_fib(n - 2, memoize);
//        return memoize[n];
//    }
//}


// Solution 3: O(n) Time | O(1) Space
int get_nth_fib(int n) {
    std::vector<int> fibonacci_numbers_pair = {0, 1};
    size_t counter = 3;

    while (counter <= n) {
        int next_fibonacci_number = fibonacci_numbers_pair[0] + fibonacci_numbers_pair[1];
        fibonacci_numbers_pair = {fibonacci_numbers_pair[1], next_fibonacci_number};
        ++counter;
    }

    return (n > 1 ? fibonacci_numbers_pair[1] : fibonacci_numbers_pair[0]);
}