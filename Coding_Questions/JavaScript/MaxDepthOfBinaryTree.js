function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

const maxDepth = (root) =>
  !root ? 0 : Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
