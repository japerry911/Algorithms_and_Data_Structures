// ---Branch Sums---

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const branchSums = (root) => {
  const sums = [];
  calcBranchSums(root, root.value, sums);
  return sums;
};

const calcBranchSums = (node, currentSum, runningSums) => {
  if (node.left !== null) {
    calcBranchSums(node.left, currentSum + node.left.value, runningSums);
  }

  if (node.right !== null) {
    calcBranchSums(node.right, currentSum + node.right.value, runningSums);
  }

  if (node.left === null && node.right === null) {
    runningSums.push(currentSum);
  }
};
