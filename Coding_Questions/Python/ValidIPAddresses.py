# ---Valid IP Addresses---

from typing import List


def valid_ip_addresses(string: str) -> List[str]:
    valid_ips_list = list()

    for f_idx in range(1, 4):
        for s_idx in range(f_idx + 1, f_idx + 4):
            for t_idx in range(s_idx + 1, len(string)):
                potential_ip_address = string[:f_idx] + "." + \
                                       string[f_idx:s_idx] + "." + \
                                       string[s_idx:t_idx] + "." + \
                                       string[t_idx:]

                if check_valid_ip_address(potential_ip_address) is True:
                    valid_ips_list.append(potential_ip_address)

    return valid_ips_list


def check_valid_ip_address(string: str) -> bool:
    split_str = string.split(".")

    for section in split_str:
        full_number = ""
        for idx, number in enumerate(section):
            if idx == 0 and number == "0" and len(section) > 1:
                return False
            full_number += number

        if int(full_number) > 255:
            return False

    return True


def check_valid_ip_section(string: str) -> bool:
    return not (int(string) > 255 or (len(string) > 1 and string[0] == "0"))


def check_list_equality(list1: List[str], list2: List[str]) -> bool:
    return len(list1) == len(list2) and sorted(list1) == sorted(list2)


input1 = "1921680"
expected1 = [
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
]
actual1 = valid_ip_addresses(input1)
print(f"EXPECTED:\t{expected1}")
print("------------------------")
print(f"ACTUAL:\t\t{actual1}")
assert check_list_equality(actual1, expected1)
