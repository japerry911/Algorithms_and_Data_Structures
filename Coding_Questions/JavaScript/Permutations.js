// ---Permutations---

// const getPermutations = (array) => {
//   let perms = [];
//   permutationHelper(array, [], perms);
//   return perms;
// };

// const permutationHelper = (array, perm, perms) => {
//   if (!array.length && perm.length) {
//     perms.push(perm);
//   } else {
//     for (let i = 0; i < array.length; i++) {
//       const newArray = array.slice(0, i).concat(array.slice(i + 1));
//       const newPermutation = perm.concat(array[i]);
//       permutationHelper(newArray, newPermutation, perms);
//     }
//   }
// };

const getPermutations = (array) => {
  const perms = [];
  permutationHelper(0, array, perms);
  return perms;
};

const permutationHelper = (idx, array, perms) => {
  if (idx === array.length - 1) {
    perms.push(array.slice());
  } else {
    for (let j = idx; j < array.length; j++) {
      swap(array, idx, j);
      permutationHelper(idx + 1, array, perms);
      swap(array, idx, j);
    }
  }
};

const swap = (array, i, j) => {
  const tmp = array[i];
  array[i] = array[j];
  array[j] = tmp;
};

console.log(getPermutations([1, 2, 3]));
