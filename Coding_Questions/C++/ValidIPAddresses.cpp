// ---Valid IP Addresses---

#include <vector>
#include <string>


bool check_ip_section(std::string section) {
    return !(stoi(section) > 255 || (section.size() > 1 && section[0] == '0'));
}


std::string join(std::vector<std::string> strings) {
    std::string s;
    for (int i = 0; i < strings.size(); ++i) {
        s += strings[i];
        if (i < strings.size() - 1) {
            s += ".";
        }
    }
    return s;
}


std::vector<std::string> valid_ip_addresses(const std::string &string) {
    std::vector<std::string> valid_ip_vector;

    for (int i = 1; i < std::min((int)string.size(), 4); ++i) {
        std::vector<std::string> ip_vector = {"", "", "", ""};

        ip_vector[0] = string.substr(0, i);

        if (!check_ip_section(ip_vector[0])) {
            continue;
        }

        for (int q = i + 1; q < i + std::min((int)string.size() - i, 4); ++q) {
            ip_vector[1] = string.substr(i + 1, q);

            if (!check_ip_section(ip_vector[1])) {
                continue;
            }

            for (int a = q + 1; a < q + std::min((int)string.size() - q, 4); ++a) {
                ip_vector[2] = string.substr(q + 1, a);
                ip_vector[3] = string.substr(a + 1, std::string::npos);

                if (check_ip_section(ip_vector[2]) && check_ip_section(ip_vector[3])) {
                    valid_ip_vector.push_back(join(ip_vector));
                }
            }
        }
    }

    return valid_ip_vector;
}
