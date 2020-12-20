// ---Bubble Sort---

const bubbleSort = (array) => {
  let counter = 0;
  while (true) {
    let swapped_occurred = false;
    for (let i = 0; i < array.length - 1 - counter; i++) {
      if (array[i] > array[i + 1]) {
        const tmp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = tmp;
        swapped_occurred = true;
      }
    }
    if (!swapped_occurred) {
      break;
    }
    counter++;
  }
  return array;
};

const input = [8, 5, 2, 9, 5, 6, 3];
console.log(bubbleSort(input));
