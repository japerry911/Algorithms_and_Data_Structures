// ---Generate Document---

const generateDocument = (characters, document) => {
  if (characters.length < document.length) {
    return false;
  } else if (document === '') {
    return true;
  }

  const characterObject = {};

  for (const char of characters) {
    if (characterObject[char] === undefined) {
      characterObject[char] = 1;
    } else {
      characterObject[char]++;
    }
  }

  for (const char of document) {
    if (characterObject[char] !== undefined) {
      characterObject[char]--;
      if (characterObject[char] < 0) {
        return false;
      }
    } else {
      return false;
    }
  }

  return true;
};

const a = generateDocument(
  'Bste!hetsi ogEAxpelrt x ',
  'AlgoExpert is the Best!'
);
console.log(a); // true
