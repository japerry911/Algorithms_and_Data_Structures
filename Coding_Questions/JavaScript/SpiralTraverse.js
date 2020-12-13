// ---Spiral Traverse---

function spiralTraverse(array) {
  let startRow = 0;
  let startColumn = 0;
  let endRow = array.length - 1;
  let endColumn = array[0].length - 1;
  const returnArray = [];

  while (startRow <= endRow && startColumn <= endColumn) {
    for (let c = startColumn; c <= endColumn; c++) {
      returnArray.push(array[startRow][c]);
    }

    for (let r = startRow + 1; r <= endRow; r++) {
      returnArray.push(array[r][endColumn]);
    }

    for (let c = endColumn - 1; c > startColumn; c--) {
      if (startRow === endRow) {
        break;
      }
      returnArray.push(array[endRow][c]);
    }

    for (let r = endRow; r > startRow; r--) {
      if (startColumn === endColumn) {
        break;
      }
      returnArray.push(array[r][startColumn]);
    }

    startRow++;
    startColumn++;
    endRow--;
    endColumn--;
  }

  return returnArray;
}

const matrix = [
  [1, 2, 3],
  [12, 13, 4],
  [11, 14, 5],
  [10, 15, 6],
  [9, 8, 7],
];
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
const actual = spiralTraverse(matrix);
console.log(actual, "\n", expected, "\n");
