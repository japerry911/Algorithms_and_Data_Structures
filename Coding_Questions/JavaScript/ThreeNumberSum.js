// ---Three Number Sum---

const threeNumberSum = (array, targetSum) => {
  const returnList = [];
  array.sort((a, b) => a - b);

  for (let i = 0; i < array.length; i++) {
    let leftPointer = i + 1;
    let rightPointer = array.length - 1;

    while (leftPointer < rightPointer) {
      const currentSum = array[i] + array[leftPointer] + array[rightPointer];

      if (currentSum < targetSum) {
        leftPointer++;
      } else if (currentSum > targetSum) {
        rightPointer--;
      } else {
        returnList.push([array[i], array[leftPointer], array[rightPointer]]);
        leftPointer++;
        rightPointer--;
      }
    }
  }

  return returnList;
};

const actual = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0);
console.log(actual); // [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
