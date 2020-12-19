// ---Binary Search---

const binarySearch = (array, target) => {
  return binarySearchHelper(array, target, 0, array.length - 1);
};

const binarySearchHelper = (array, target, leftPointer, rightPointer) => {
  while (leftPointer <= rightPointer) {
    const middlePoint = Math.floor((leftPointer + rightPointer) / 2);
    if (array[middlePoint] === target) {
      return middlePoint;
    } else if (array[middlePoint] > target) {
      rightPointer = middlePoint - 1;
    } else if (array[middlePoint] < target) {
      leftPointer = middlePoint + 1;
    }
  }
  return -1;
};

console.log(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)); // 3
