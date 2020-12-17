// ---Count Number of Consistent Strings---

const countConsistentStrings = (allowed, words) => {
  let consistentStrings = words.length;

  for (const word of words) {
    for (const character of word) {
      if (allowed.indexOf(character) === -1) {
        consistentStrings--;
        break;
      }
    }
  }

  return consistentStrings;
};

const words1 = ["ad", "bd", "aaab", "baa", "badab"];
const allowed1 = "ab";
const actual = countConsistentStrings(allowed1, words1);
const expected = 2;
console.log(actual, "===", expected);
