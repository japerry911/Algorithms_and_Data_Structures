// ---Longest Palindromic Substring---


bool is_palindromic(std::string str) {
    std::string str_original = str;
    std::reverse(str.begin(), str.end());
    return str_original == str;
}



std::string longest_palindromic_substring(std::string str) {
    std::string longest_palindrome(1, str[0]);

    for (size_t i = 0; i < str.length(); ++i) {
        for (size_t r = i; r < str.length(); ++r) {
            if (is_palindromic(str.substr(i, r + 1)) and str.substr(i, r + 1).length() > longest_palindrome.length()) {
                longest_palindrome = str.substr(i, r + 1);
            }
        }
    }

    return longest_palindrome;
}