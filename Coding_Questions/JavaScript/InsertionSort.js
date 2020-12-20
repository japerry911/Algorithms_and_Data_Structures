// ---Insertion Sort---

const insertionSort = (array) => {
  for (let i = 1; i < array.length; i++) {
    let counter = 0;
    for (let j = i - 1; j >= 0; j--) {
      if (array[i - counter] < array[j]) {
        swap(array, i - counter, j);
        counter++;
      } else {
        break;
      }
    }
  }
  return array;
};

const swap = (array, i, j) => {
  const tmp = array[i];
  array[i] = array[j];
  array[j] = tmp;
};

const input = [8, 5, 2, 9, 5, 6, 3];
console.log(insertionSort(input));
