// ---Smallest Difference---

const smallestDifference = (arrayOne, arrayTwo) => {
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  let pointer1 = 0;
  let pointer2 = 0;

  let currentSmallest = [null, Infinity];

  while (pointer1 < arrayOne.length && pointer2 < arrayTwo.length) {
    const pairs_difference = calculateDifference(
      arrayOne[pointer1],
      arrayTwo[pointer2]
    );

    if (pairs_difference === 0) {
      return [arrayOne[pointer1], arrayTwo[pointer2]];
    }

    if (pairs_difference < currentSmallest[1]) {
      currentSmallest = [
        [arrayOne[pointer1], arrayTwo[pointer2]],
        pairs_difference,
      ];
    }

    if (arrayOne[pointer1] < arrayTwo[pointer2]) {
      pointer1++;
    } else {
      pointer2++;
    }
  }

  return currentSmallest[0];
};

const calculateDifference = (num1, num2) => Math.abs(num1 - num2);

console.log(
  smallestDifference(
    [240, 124, 86, 111, 2, 84, 954, 27, 89],
    [1, 3, 954, 19, 8]
  )
); // [-123, -124]
