// ---Same BSTs---

const sameBsts = (arrayOne, arrayTwo) => {
  if (arrayOne.length === 0 && arrayTwo.length === 0) {
    return true;
  } else if (
    arrayOne.length !== arrayTwo.length ||
    arrayOne[0] !== arrayTwo[0]
  ) {
    console.log(arrayOne, arrayTwo);
    return false;
  } else if (arrayOne.length === 1 && arrayTwo.length === 1) {
    return arrayOne[0] === arrayTwo[0];
  }

  const rootValue1 = arrayOne.shift();
  const rootValue2 = arrayTwo.shift();

  const leftSubtreeValues1 = arrayOne.filter((element) => element < rootValue1);
  const leftSubtreeValues2 = arrayTwo.filter((element) => element < rootValue2);
  const rightSubtreeValues1 = arrayOne.filter(
    (element) => element >= rootValue1
  );
  const rightSubtreeValues2 = arrayTwo.filter(
    (element) => element >= rootValue2
  );

  return (
    sameBsts(leftSubtreeValues1, leftSubtreeValues2) &&
    sameBsts(rightSubtreeValues1, rightSubtreeValues2)
  );
};

const arrayOne = [50, 76, 81, 23, 23, 23, 100, 56, 12, -1, 3];
const arrayTwo = [50, 23, 76, 23, 23, 12, 56, 81, -1, 3, 100];
const actual = sameBsts(arrayOne, arrayTwo);
console.log(actual); // true
