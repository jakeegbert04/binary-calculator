def bin_add(bin_str_1, bin_str_2):

    max_len = max(len(bin_str_1), len(bin_str_2))

    bin_str_1 = bin_str_1.zfill(max_len)
    bin_str_2 = bin_str_2.zfill(max_len)

    bin_str_1_rev = bin_str_1[::-1]
    bin_str_2_rev = bin_str_2[::-1]

    result = ""
    carry = False
    for index, num2 in enumerate(bin_str_2_rev):
        num1 = bin_str_1_rev[index]
        if carry == False:

            if num1 == "0" and num2 == "0":
                result += "0"
                continue
            elif num1 == "1" and num2 == "0":
                result += "1"
                continue

            elif num1 == "0" and num2 == "1":
                result += "1"
                continue

            elif num1 == "1" and num2 == "1":
                result += "0"
                carry = True
                continue

        if carry == True:
            if num1 == "0" and num2 == "0":
                result += "1"
                carry = False
                continue
            elif num1 == "1" and num2 == "0":
                result += "0"
                carry = True
                continue
            elif num1 == "0" and num2 == "1":
                result += "0"
                carry = True
                continue
            elif num1 == "1" and num2 == "1":
                result += "1"
                carry = True
                continue
    if carry:
        result += "1"

    result = result[::-1]
    return result


def bin_mul(bin_str_1, bin_str_2):
    max_len = max(len(bin_str_1), len(bin_str_2))

    bin_str_1 = bin_str_1.zfill(max_len)
    bin_str_2 = bin_str_2.zfill(max_len)

    bin_str_1_rev = bin_str_1[::-1]
    bin_str_2_rev = bin_str_2[::-1]
    count = "0"
    number = "0"
    place_holder = ""
    for digit in bin_str_2_rev:
        if digit == "1":
            count = bin_str_1 + place_holder
        else:
            count = "0"
        place_holder += "0"
        number = bin_add(count, number)
    return number


print(bin_mul("100010", "101100"))
