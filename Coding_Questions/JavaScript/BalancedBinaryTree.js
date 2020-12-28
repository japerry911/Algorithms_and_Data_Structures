function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

const isBalanced = (root) => {
  if (!root) {
    return true;
  }

  const left = maxDepth(root.left);
  const right = maxDepth(root.right);

  const currentStatus = Math.abs(left - right) <= 1;

  return currentStatus && isBalanced(root.left) && isBalanced(root.right);
};

const maxDepth = (root) =>
  !root ? 0 : Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
