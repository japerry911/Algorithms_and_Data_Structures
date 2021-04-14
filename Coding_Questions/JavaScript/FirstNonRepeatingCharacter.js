// ---First Non-Repeating Character---

const firstNonRepeatingCharacter = (string) => {
  const characterCount = {};

  for (const char of string) {
    if (characterCount[char] === undefined) {
      characterCount[char] = 1;
    } else {
      characterCount[char]++;
    }
  }

  for (let i = 0; i < string.length; i++) {
    if (characterCount[string[i]] === 1) {
      return i;
    }
  }

  return -1;
};

const a = firstNonRepeatingCharacter('abcdcaf');
console.log(a); // 1
