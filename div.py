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


# print(bin_dec_convert("1001"))


# if bin_dec_convert(new_number) >= bin_dec_convert(bin_str_1):
#     new_number = bin_sub(new_number, bin_str_1)
#     quotient += "1"


"""
      00001101 r1
    ----------
1101| 10101010
       1101
       ----
      
       01112
        1101
      ------
        001100
          1101
          ----
          0001

"""

print(bin_div("10101010", "1101"))
# bin_str_1_rev = bin_str_1[::-1]
# bin_str_2_rev = bin_str_2[::-1]
# result = ''
# for bin_str_2  in bin_str_1:
#   pass
# if bin_str_1 >= bin_str_2:
#     pass
# if digit in bin_str_2_rev == x in bin_str_1_rev:
# if digit in bin_str_2_rev == '0' and x in bin_str_1_rev == '1':
#   result = '1'
