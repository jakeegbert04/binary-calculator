def bin_sub(bin_str_1, bin_str_2):

    max_len = max(len(bin_str_1), len(bin_str_2))
    bin_str_1 = bin_str_1.zfill(max_len)
    bin_str_2 = bin_str_2.zfill(max_len)
    bin_str_1_rev = bin_str_1[::-1]
    bin_str_2_rev = bin_str_2[::-1]
    result = ""
    borrow = False
    for index, num2 in enumerate(bin_str_2_rev):
        num1 = bin_str_1_rev[index]
        if num1 > num2:
            result = "error, negative number"
            return result
        elif borrow == False:
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
            # elif num1 > num2:
            #     result += "1"
            #     borrow = False
            #     continue
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


print(bin_sub("01010", "10111"))
# for x, z in bin_str_1, bin_str_2:
#     if x == "0" and z == "1":
#         result == "1"

# result == '0'
# num1 = ''
# borrow = False


# Here's a hint for the Subtraction Logic:
# If both digits are equal to each other, the result will always be 0.
# If the digits are not equal to each other, the result will always be a 1.
# If the first digit is less than the second digit, we know we will need to borrow.
# Borrowing will continue until we reach a 1 in our first digit. (edited)


# if num1 == num2:
#     result = "0"
#     borrow = False
# if num1 != num2:
#     result = "1"
#     borrow = False
# if num1 < num2:
#     result = "0"
#     borrow = True
