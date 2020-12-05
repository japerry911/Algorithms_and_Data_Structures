// ---Caesar Cipher Encryptor---


std::string caesar_cypher_encryptor(std::string str, int key) {
    std::string encrypted_text;

    for (const auto c : str) {
        int ascii_number = (int)c + key;

        if (ascii_number > 122) {
            while (ascii_number > 122) {
                ascii_number %= 122;
                ascii_number += 96;
            }
        }

        encrypted_text += (char)ascii_number;
    }

    return encrypted_text;
}