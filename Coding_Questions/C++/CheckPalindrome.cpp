// ---Check Palindrome---


bool is_palindrome(std::string str) {
    std::string str_original = str;
    std::reverse(str.begin(), str.end());
    return str_original == str;
}

