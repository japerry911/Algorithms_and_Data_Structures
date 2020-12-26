// ---Powerset---

const powerset = (array) => {
  const subsets = [[]];

  for (let element of array) {
    const subsetLength = subsets.length;
    for (let i = 0; i < subsetLength; i++) {
      subsets.push([...subsets[i], element]);
    }
  }

  return subsets;
};

const input = [1, 2, 3];
const expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]];
const actual = powerset(input);
console.log(actual, expected);
