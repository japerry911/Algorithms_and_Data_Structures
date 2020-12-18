// ---Permutations---

const getPermutations = (array) => {
  let perms = [];
  permutationHelper(array, [], perms);
  return perms;
};

const permutationHelper = (array, perm, perms) => {
  if (!array.length && perm.length) {
    perms.push(perm);
  } else {
    for (let i = 0; i < array.length; i++) {
      const newArray = array.slice(0, i).concat(array.slice(i + 1));
      const newPermutation = perm.concat(array[i]);
      permutationHelper(newArray, newPermutation, perms);
    }
  }
};

console.log(getPermutations([1, 2, 3]));
