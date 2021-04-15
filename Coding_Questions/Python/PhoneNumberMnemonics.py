# ---Phone Number Mnemonics---

from typing import List

NUMBER_MAP = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def phone_number_mnemonics(phone_number: str) -> List[str]:
    mnemonics = list()
    phone_number_mnemonics_helper(
        0,
        phone_number,
        ["0"] * len(phone_number),
        mnemonics
    )

    return mnemonics


def phone_number_mnemonics_helper(
        idx: int,
        phone_number: str,
        current_mnemonic: List[str],
        mnemonics: List[str]
):
    if idx >= len(phone_number):
        mnemonics.append("".join(current_mnemonic))
        return

    possibilities = NUMBER_MAP[phone_number[idx]]

    for char in possibilities:
        current_mnemonic[idx] = char
        phone_number_mnemonics_helper(
            idx + 1,
            phone_number,
            current_mnemonic,
            mnemonics
        )


a = phone_number_mnemonics("1905")
print(a)
# ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l",
#  "1z0j", "1z0k", "1z0l"]
