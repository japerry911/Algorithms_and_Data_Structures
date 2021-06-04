def reverse(x: int) -> int:
    start = ""
    if 0 > x > -2_147_483_648:
        x = abs(x)
        start = "-"
    elif x == 0 or x > 2_147_483_647 or x <= -2_147_483_648:
        return 0

    ret = list()

    while x > 0:
        ret.append(str(x % 10))
        x //= 10

    result = int(start + ("".join(ret)))

    if result > 2_147_483_647 or result <= -2_147_483_648:
        return 0
    else:
        return result


input_value = 1463847412  # -1534236470
expected_output_value = 2147483641
output_value = reverse(input_value)
print(output_value, "==", expected_output_value)
assert output_value == expected_output_value
