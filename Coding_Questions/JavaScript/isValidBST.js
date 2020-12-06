// ---Is Valid BST---

var isValidBST = function (root, minValue = -Infinity, maxValue = Infinity) {
  if (!isValidBSTHelper(root, minValue, maxValue)) {
    return false;
  }

  if (root.left !== null) {
    if (!isValidBST(root.left, minValue, root.val)) {
      return false;
    }
  }

  if (root.right !== null) {
    if (!isValidBST(root.right, root.val, maxValue)) {
      return false;
    }
  }

  return true;
};

function isValidBSTHelper(node, minValue, maxValue) {
  return minValue < node.val && node.val < maxValue;
}
