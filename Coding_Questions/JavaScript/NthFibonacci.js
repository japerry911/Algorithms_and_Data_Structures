// ---Nth Fibonacci---

// Solution 1: O(2^n) Time | O(n) Space
// function getNthFib(n) {
//   if (n == 1) {
//     return 0;
//   } else if (n == 2) {
//     return 1;
//   } else {
//     return getNthFib(n - 1) + getNthFib(n - 2);
//   }
// }

// Solution 2: O(n) Time | O(n) Space)
// function getNthFib(n, memoize = { 1: 0, 2: 1 }) {
//   if (n in memoize) {
//     return memoize[n];
//   } else {
//     memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize);
//     return memoize[n];
//   }
// }

// Solution 3: O(n) Time | O(1) Space)
function getNthFib(n) {
  let fibNumbsPair = [0, 1];
  let counter = 3;

  while (counter <= n) {
    const nextFibNumb = fibNumbsPair[0] + fibNumbsPair[1];
    fibNumbsPair = [fibNumbsPair[1], nextFibNumb];
    ++counter;
  }

  return n > 1 ? fibNumbsPair[1] : fibNumbsPair[0];
}

console.log(getNthFib(6)); // 5
