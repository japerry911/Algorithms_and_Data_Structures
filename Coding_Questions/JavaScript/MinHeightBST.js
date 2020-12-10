// ---Min Height BST---

class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    let currentNode = this;

    while (true) {
      if (value < currentNode.value) {
        if (currentNode.left === null) {
          currentNode.left = new BST(value);
          break;
        } else {
          currentNode = currentNode.left;
        }
      } else {
        if (currentNode.right === null) {
          currentNode.right = new BST(value);
          break;
        } else {
          currentNode = currentNode.right;
        }
      }
    }

    return this;
  }
}

function constructMinHeightBst(array, startIndex, endIndex) {
  if (endIndex < startIndex) {
    return null;
  }

  const middleIndex = Math.floor((startIndex + endIndex) / 2);
  const bst = new BST(array[middleIndex]);

  bst.left = constructMinHeightBst(array, startIndex, middleIndex - 1);
  bst.right = constructMinHeightBst(array, middleIndex + 1, endIndex);

  return bst;
}

function minHeightBst(array) {
  return constructMinHeightBst(array, 0, array.length - 1);
}
