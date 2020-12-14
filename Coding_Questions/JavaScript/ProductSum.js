// ---Product Sum---

const productSum = (array, depth = 1) => {
  let runningSum = 0;

  for (const element of array) {
    if (Array.isArray(element)) {
      runningSum += productSum(element, depth + 1);
    } else {
      runningSum += element;
    }
  }

  return runningSum * depth;
};
