// ---Find Duplicate Value---

const firstDuplicateValue = (array) => {
  const holdingSet = new Set();

  for (const element of array) {
    if (holdingSet.has(element)) {
      return element;
    }
    holdingSet.add(element);
  }

  return -1;
};

const input = [2, 1, 5, 2, 3, 3, 4];
const actual = firstDuplicateValue(input);
console.log(actual); // 2
