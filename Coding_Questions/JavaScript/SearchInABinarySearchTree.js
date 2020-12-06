// ---Search in a Binary Search Tree---

var searchBST = function (root, val) {
  let current_node = root;

  while (current_node !== null) {
    if (val > current_node.val) {
      current_node = current_node.right;
    } else if (val < current_node.val) {
      current_node = current_node.left;
    } else {
      return current_node;
    }
  }

  return null;
};
