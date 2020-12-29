// ---Same BSTs---

const sameBsts = (arrayOne, arrayTwo) => {
  if (!arrayOne.length && !arrayTwo.length) {
    return true;
  } else if (
    arrayOne.length !== arrayTwo.length ||
    arrayOne[0] !== arrayTwo[0]
  ) {
    return false;
  } else if (arrayOne.length === 1 && arrayTwo.length === 1) {
    return arrayOne[0] === arrayTwo[0];
  }

  const rootValue1 = arrayOne.shift();
  const rootValue2 = arrayTwo.shift();

  const leftSubtreeValues1 = arrayOne.filter((element) => element < rootValue1);
  const leftSubtreeValues2 = arrayTwo.filter(
    (element) => element <= rootValue2
  );
  const rightSubtreeValues1 = arrayOne.filter(
    (element) => element >= rootValue1
  );
  const rightSubtreeValues2 = arrayTwo.filter(
    (element) => element >= rootValue2
  );

  if (
    leftSubtreeValues1.sort((a, b) => a - b) !==
    leftSubtreeValues2.sort((a, b) => a - b)
  ) {
    return false;
  }
  if (
    rightSubtreeValues1.sort((a, b) => a - b) !==
    rightSubtreeValues2.sort((a, b) => a - b)
  ) {
    return false;
  }

  console.log(rightSubtreeValues2);

  return (
    sameBsts(leftSubtreeValues1, leftSubtreeValues2) &&
    sameBsts(rightSubtreeValues1, rightSubtreeValues2)
  );
};

const arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11];
const arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81];
const actual = sameBsts(arrayOne, arrayTwo);
console.log(actual); // true
