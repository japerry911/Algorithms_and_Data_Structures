// ---Node Depths---

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const nodeDepths = (root, depth = 0) => {
  return (
    depth +
    (root.left === null ? 0 : nodeDepths(root.left, depth + 1)) +
    (root.right === null ? 0 : nodeDepths(root.right, depth + 1))
  );
};
