# ---Caesar Cipher Encryptor---
# all letters are LOWERCASE


def caesar_cipher_encryptor(string: str, key: int) -> str:
    output = ""
    for char in string:
        ascii_number = ord(char) + key
        if ascii_number > 122:
            while ascii_number > 122:
                ascii_number %= 122
                ascii_number += 96
        output += chr(ascii_number)
    return output


def caesar_cipher_encryptor2(string: str, key: int) -> str:
    return "".join(list(
        map(lambda x: caesar_cipher_encryptor2_helper(x, key), list(string))
    ))


def caesar_cipher_encryptor2_helper(char: str, key: int) -> chr:
    ascii_number = ord(char) + key
    if ascii_number > 122:
        while ascii_number > 122:
            ascii_number %= 122
            ascii_number += 96
    return chr(ascii_number)


print(caesar_cipher_encryptor2("abc", 52))  # "zab"
