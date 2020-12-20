// ---Find Three Largest Numbers---

const findThreeLargestNumbers = (array) => {
  const threeLargestNumbers = [null, null, null];
  for (const element of array) {
    updateLargest(threeLargestNumbers, element);
  }
  return threeLargestNumbers;
};

const updateLargest = (threeLargestNumbers, element) => {
  if (threeLargestNumbers[2] === null || threeLargestNumbers[2] < element) {
    shiftAndUpdate(threeLargestNumbers, element, 2);
  } else if (
    threeLargestNumbers[1] === null ||
    threeLargestNumbers[1] < element
  ) {
    shiftAndUpdate(threeLargestNumbers, element, 1);
  } else if (
    threeLargestNumbers[0] === null ||
    threeLargestNumbers[0] < element
  ) {
    shiftAndUpdate(threeLargestNumbers, element, 0);
  }
};

const shiftAndUpdate = (threeLargestNumbers, element, idx) => {
  for (let i = 0; i < idx; i++) {
    threeLargestNumbers[i] = threeLargestNumbers[i + 1];
  }
  threeLargestNumbers[idx] = element;
};

console.log(
  findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
); // [18, 141, 541]
