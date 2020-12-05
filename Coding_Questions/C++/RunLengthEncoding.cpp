// ---Run-Length Encoding---


std::string run_length_encoding(std::string str) {
    std::string encoding;
    char previous_char = str[0];
    size_t counter = 1;

    for (size_t i = 1; i < str.length(); ++i) {
        if (str[i] == previous_char) {
            ++counter;

            if (counter > 9) {
                encoding += std::to_string(9) + previous_char;
                counter = 1;
            }
        } else {
            encoding += std::to_string(counter) + previous_char;
            previous_char = str[i];
            counter = 1;
        }
    }

    encoding += std::to_string(counter) + previous_char;

    return encoding;
}