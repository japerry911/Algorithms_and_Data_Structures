// ---Max Subset Sum No Adjacent---

const maxSubsetSumNoAdjacent = (array) => {
  if (array.length === 0) {
    return 0;
  }

  for (let i = 2; i < array.length; i++) {
    array[i] += Math.max(...array.slice(0, i - 1));
  }

  return Math.max(...array);
};

console.log(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])); // 330
