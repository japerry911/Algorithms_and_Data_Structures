# ---Run Length Encoding---


def run_length_encoding(string: str) -> str:
    encoded_string = ""
    previous_char = string[0]
    counter = 0

    for char in string:
        if char == previous_char:
            counter += 1

            if counter > 9:
                encoded_string += f"9{previous_char}"
                counter = 1

            continue
        encoded_string += str(counter) + previous_char
        previous_char = char
        counter = 1

    encoded_string += str(counter) + previous_char

    return encoded_string


input_string = "AAAAAAAAAAAAABBCCCCDD"
expected = "9A4A2B4C2D"
actual = run_length_encoding(input_string)
print(actual)
assert actual == expected
