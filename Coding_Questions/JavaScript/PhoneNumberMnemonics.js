// ---Phone Number Mnemonics---

const NUMBER_MAP = {
  0: ['0'],
  1: ['1'],
  2: ['a', 'b', 'c'],
  3: ['d', 'e', 'f'],
  4: ['g', 'h', 'i'],
  5: ['j', 'k', 'l'],
  6: ['m', 'n', 'o'],
  7: ['p', 'q', 'r', 's'],
  8: ['t', 'u', 'v'],
  9: ['w', 'x', 'y', 'z'],
};

const phoneNumberMnemonics = (phoneNumber) => {
  let mnemonics = [];
  let currentMnemonic = new Array(phoneNumber.length);

  phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonics);

  return mnemonics;
};

const phoneNumberMnemonicsHelper = (
  idx,
  phoneNumber,
  currentMnemonic,
  mnemonics
) => {
  if (idx >= phoneNumber.length) {
    mnemonics.push(currentMnemonic.join(''));
    return;
  }

  for (const char of NUMBER_MAP[phoneNumber[idx]]) {
    currentMnemonic[idx] = char;
    phoneNumberMnemonicsHelper(
      idx + 1,
      phoneNumber,
      currentMnemonic,
      mnemonics
    );
  }
};

const a = phoneNumberMnemonics('1905');
console.log(a);
// ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
