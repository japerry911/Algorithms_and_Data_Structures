// ---Underscorify Substring---

const underscorifySubstring = (string, substring) => {
  const locations2DArray = getLocations(string, substring);
  const collapsedLocations2DArray = collapseLocations(locations2DArray);
  const returnString = underscorify(string, collapsedLocations2DArray);
  return returnString;
};

const getLocations = (string, substring) => {
  const locations2DArray = [];
  let currentIdx = 0;

  while (currentIdx < string.length) {
    const idxReturn = string.indexOf(substring, currentIdx);
    if (idxReturn !== -1) {
      locations2DArray.push([idxReturn, idxReturn + substring.length]);
      currentIdx = idxReturn + 1;
    } else {
      break;
    }
  }

  return locations2DArray;
};

const collapseLocations = (locations2DArray) => {
  const collapsedLocations2DArray = [];
  let firstRun = true;

  for (const locationSubArray of locations2DArray) {
    if (firstRun) {
      collapsedLocations2DArray.push(locationSubArray);
      firstRun = false;
    } else {
      if (
        collapsedLocations2DArray[collapsedLocations2DArray.length - 1][1] >=
        locationSubArray[0]
      ) {
        collapsedLocations2DArray[collapsedLocations2DArray.length - 1][1] =
          locationSubArray[1];
      } else {
        collapsedLocations2DArray.push(locationSubArray);
      }
    }
  }

  return collapsedLocations2DArray;
};

const underscorify = (string, collapsedLocations2DArray) => {
  let underscoresAdded = 0;

  for (const locationSubArray of collapsedLocations2DArray) {
    string =
      string.slice(0, locationSubArray[0] + underscoresAdded) +
      "_" +
      string.slice(
        locationSubArray[0] + underscoresAdded,
        locationSubArray[1] + underscoresAdded
      ) +
      "_" +
      string.slice(locationSubArray[1] + underscoresAdded);
    underscoresAdded += 2;
  }

  return string;
};

const actual = underscorifySubstring(
  "testthis is a testtest to see if testestest it works",
  "test"
);
const expected = "_test_this is a _testtest_ to see if _testestest_ it works";
console.log("EXPECTED:\t", expected);
console.log("ACTUAL:\t\t", actual);
console.log(expected === actual);
