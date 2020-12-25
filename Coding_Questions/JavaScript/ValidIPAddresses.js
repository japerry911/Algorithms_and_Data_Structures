// ---Valid IP Addresses---

const validIPAddresses = (string) => {
  const validIPArray = [];

  for (let i = 1; i < Math.min(string.length, 4); i++) {
    const ipAddressSectionsArray = ["", "", "", ""];

    ipAddressSectionsArray[0] = string.slice(0, i);

    if (!checkIPAddressSection(ipAddressSectionsArray[0])) {
      continue;
    }

    for (let c = i + 1; c < i + Math.min(string.length - i, 4); c++) {
      ipAddressSectionsArray[1] = string.slice(i, c);

      if (!checkIPAddressSection(ipAddressSectionsArray[1])) {
        continue;
      }

      for (let r = c + 1; r < c + Math.min(string.length - c, 4); r++) {
        ipAddressSectionsArray[2] = string.slice(c, r);
        ipAddressSectionsArray[3] = string.slice(r, string.length);

        if (
          checkIPAddressSection(ipAddressSectionsArray[2]) &&
          checkIPAddressSection(ipAddressSectionsArray[3])
        ) {
          validIPArray.push(ipAddressSectionsArray.join("."));
        }
      }
    }
  }

  return validIPArray;
};

const checkIPAddressSection = (section) => {
  return !(
    parseInt(section) > 255 ||
    (section[0] === "0" && section.length > 1)
  );
};

const checkIfListsAreEqual = (list1, list2) => {
  if (list1.length !== list2.length) {
    return false;
  }
  for (let i = 0; i < list1.length; i++) {
    if (list1[i] !== list2[i]) {
      return false;
    }
  }
  return true;
};
const input = "1921680";
const expected = [
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0",
];
const actual = validIPAddresses(input);
console.log(checkIfListsAreEqual(actual, expected));
