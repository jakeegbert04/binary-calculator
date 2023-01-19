def dec_bin_convert(dec_num):

    if not dec_num in range(0, 256):
        return f"Not in range"
    binary_number = ""
    list_of_bits = [128, 64, 32, 16, 8, 4, 2, 1]
    for bit in list_of_bits:
        if dec_num >= bit:
            binary_number += "1"
            dec_num -= bit
        else:
            binary_number += "0"

    return binary_number


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


def bin_sub(bin_str_1, bin_str_2):

    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_str_1 = bin_str_1.zfill(max_len)
    bin_str_2 = bin_str_2.zfill(max_len)
    bin_str_1_rev = bin_str_1[::-1]
    bin_str_2_rev = bin_str_2[::-1]
    result = ""
    borrow = False
    if bin_dec_convert(bin_str_2) > bin_dec_convert(bin_str_1):
        return "Error, Negative Number"
    for index, num2 in enumerate(bin_str_2_rev):
        num1 = bin_str_1_rev[index]
        # if bin_dec_convert(num1) > bin_dec_convert(num2):
        #     result = "error, negative number"
        #     return result
        if borrow == False:
            if num1 == num2:
                result += "0"
                borrow = False
                continue
            elif num1 != num2:
                result += "1"
                if num1 < num2:
                    borrow = True
                    continue
                else:
                    borrow = False
                    continue
            elif num1 < num2:
                result += "0"
                borrow = True
                continue
        elif borrow == True:
            if num1 == "0" and num2 == "1":
                result += "0"
                borrow = True
                continue

            elif num1 == "0" and num2 == "0":
                result += "1"
                borrow = True
                continue
            elif num1 == "1":

                if num2 == "1":
                    borrow = True
                    result += "1"
                    continue
                elif num2 == "0":
                    result += "0"
                    borrow = False
                    continue
    return result[-1::-1]


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


def bin_div(bin_str_2, bin_str_1):
    new_number = ""
    quotient = ""

    for digit in bin_str_2:

        new_number += digit
        if bin_dec_convert(new_number) >= bin_dec_convert(bin_str_1):
            new_number = bin_sub(new_number, bin_str_1)
            quotient += "1"
        else:
            quotient += "0"

    return f"{quotient} with a remainder of {new_number}"


def bin_dec_convert(bin_str):
    base_int = 0
    bit_val = 128
    # if len(bin_str) != 8:
    #     return "That is not a valid number"
    for num in bin_str.zfill(8):
        if num == "1":
            base_int += bit_val

        bit_val = int(bit_val / 2)
    return base_int


while True:
    print(
        """
    1. Binary to Decimal Conversion
    2. Decimal to Binary Conversion
    3. Add two Binary Numbers
    4. Subtract two Binary Numbers
    5. Multiply two Binary Numbers
    6. Divide two Binary Numbers
    7. Quit

    """
    )
    main_input = input("What would you like to do?: ")
    if main_input == "1":
        user_dec_input = input("Please enter a number between 0 and 255: ")
        print(dec_bin_convert(user_dec_input))
    elif main_input == "2":
        user_bin_input = input("Please enter a 8 bit binary number: ")
        print(bin_dec_convert(user_bin_input))
    elif main_input == "3":
        user_add1_input = input("Enter the first binary number:  ")
        user_add2_input = input("Enter the first binary number:  ")
        print(bin_add(user_add1_input, user_add2_input))

    elif main_input == "4":
        user_sub1_input = input("Enter the first binary number:  ")
        user_sub2_input = input("Enter the second binary number:  ")
        print(bin_sub(user_sub1_input, user_sub2_input))
    elif main_input == "5":
        user_mult1_input = input("Enter the first binary number: ")
        user_mult2_input = input("Enter the second binary number: ")
        print(bin_mul(user_mult1_input, user_mult2_input))
    elif main_input == "6":
        user_div2_input = input("Enter a number to dividend:  ")
        user_div1_input = input("Enter a number to divisor:  ")
        print(bin_div(user_div2_input, user_div1_input))
    elif main_input == "7":
        print("Program Terminated")
        break
    else:
        print("Please choose a number on the menu.")
