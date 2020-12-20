// ---Selection Sort---

const selectionSort = (array) => {
  for (let i = 0; i < array.length; i++) {
    let pointer = i;
    for (let c = i + 1; c < array.length; c++) {
      if (array[pointer] > array[c]) {
        pointer = c;
      }
    }
    swap(array, i, pointer);
  }
  return array;
};

const swap = (array, i, j) => {
  const tmp = array[i];
  array[i] = array[j];
  array[j] = tmp;
};

const input = [8, 5, 2, 9, 5, 6, 3];
console.log(selectionSort(input));
