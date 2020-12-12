// ---Balance Binary Search Tree---

function TreeNode(val, left = null, right = null) {
  this.val = val;
  this.left = left;
  this.right = right;
}

const balanceBST = (root) => {
  const treeIntList = inOrderTraversalBST(root, []);
  return constructBalancedBST(treeIntList, 0, treeIntList.length - 1);
};

const inOrderTraversalBST = (tree, list) => {
  if (tree !== null && tree !== undefined) {
    inOrderTraversalBST(tree.left, list);
    list.push(tree.val);
    inOrderTraversalBST(tree.right, list);
  }
  return list;
};

// treeIntList => tree in order travel list
const constructBalancedBST = (treeIntList, startIndex, endIndex) => {
  if (endIndex < startIndex) {
    return null;
  }

  const middleIndex = Math.floor((startIndex + endIndex) / 2);
  const middleValue = treeIntList[middleIndex];

  const bst = new TreeNode(middleValue);

  bst.left = constructBalancedBST(treeIntList, startIndex, middleIndex - 1);
  bst.right = constructBalancedBST(treeIntList, middleIndex + 1, endIndex);

  return bst;
};
