# print("***Binary Calculator***")
# print("-----------------------")
# print("(B)inary to Decimal conversion")
# print("(D)ecimal to binary conversion")
# print("(A)dd two binary numbers")
# print("(S)ubtract two binary numbers")
# print("(M)ultiply two binary numbers")
# print("(D)ivide two binary numbers")
# print("(Q)uit")

# def dec_bin_convert(dec_num):

#     if not dec_num in range(0, 256):
#         return f"Not in range"
#     binary_number = ""
#     list_of_bits = [128, 64, 32, 16, 8, 4, 2, 1]
#     for bit in list_of_bits:
#         if dec_num >= bit:
#             binary_number += "1"
#             dec_num -= bit
#         else:
#             binary_number += "0"

#     return binary_number


# user_input = int(input("Please enter a number between 0 to 255: "))

# print(dec_bin_convert(user_input))
# # ******************************************************************************************************
# # ******************************************************************************************************
# def bin_dec_convert(bin_str):
#     base_int = 0
#     bit_val = 128
#     if len(bin_str) != 8:
#         return "That is not a valid number"
#     for num in bin_str:
#         # "11110011"
#         if num == "1":
#             base_int += bit_val

#         #   bit_val /= 2
#         bit_val = int(bit_val / 2)
#     return base_int


# user_bin_input = input("Please enter a 8 bit binary number: ")
# print(bin_dec_convert(user_bin_input))

# Verify both strings are the same length (look at zfill)
# Add some kind of carry logic
# make a truth chart (every possible outcome)
# carry variable?
# are you adding adding from left to right or right to left?

# Chart:

# Carry Off
# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 1 = 0 Turn on Carry

# Carry On
# 0 + 0 = 1 Turn off Carry

# shifted_num = "0"
# shifted_num = shifted_num[-1::-1]

# if (
#     (num1 == "1" and num2 == "1" and shifted_num == "0")
#     or (num1 == "1" and num2 == "0" and shifted_num == "1")
#     or (num1 == "1" and num2 == "1" and shifted_num == "1")
#     or (num1 == "0" and num2 == "1" and shifted_num == "1")
# ):
# carry == True

from operator import index


def bin_add(bin_str_1, bin_str_2):
    # max_len = max(bin_str_1, bin_str_2, key=len)
    max_len = max(len(bin_str_1), len(bin_str_2))
    # max_len = max_len.zfill(max_len)
    bin_str_1 = bin_str_1.zfill(max_len)
    bin_str_2 = bin_str_2.zfill(max_len)
    # max_len = long.zfill(long)
    bin_str_1_rev = bin_str_1[::-1]
    bin_str_2_rev = bin_str_2[::-1]
    # len()
    # zfill()
    # max()
    result = ""
    carry = False
    for index, num2 in enumerate(bin_str_2_rev):
        num1 = bin_str_1_rev[index]
        if carry == False:
            # shifted_num = "0"
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
            # elif num1 == "0" and num2 == "0" and shifted_num == "1":
            #     result += "1"

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


print(bin_add("1010101010", "10100100"))

# for idx, i in enumerate(bin_str_2_rev):

#     if carry == True:
#         if bin_str_1_rev[idx] == i and i == "0" and length[idx]:
#             result += "1"
#             carry = False
# """
# 0 0 1 1
# 0 1 0 1
# - - - -
# 0 1 1 0
# X X X C


# Carry Rules:
# 1 1 1 1
# 0 1 0 1
# 0 0 1 1
# - - - -
# 1 0 0 1
# X C C C
# """

# elif bin_str_1_rev == "0" and bin_str_2_rev == "1" and length == "0":
#     carry = False
# elif bin_str_1_rev == "1" and bin_str_2_rev == "0" and length == "0":
#     carry = False
# else:
#     carry = True
#     # length += "1"

#     else:

#         if i == bin_str_1_rev[idx] and i == "1":
#             result += "0"
#             carry = True

#         elif i == bin_str_1_rev[idx] and i == "0":
#             result += "0"

# return result


# 100010
#  10011
#  11001

# def bin_add(bin_str_1, bin_str_2):
#   result = ""
#   print(bin_str_1)
#   print(bin_str_2)
#   for index, i in enumerate(bin_str_2):
#       print(bin_str_1[index])
#       if i == bin_str_1[0] and i == "1":
#           result += "0"
#
#
#    for index, i in bin_str_2:
# print(bin_str_1[index])
# if i == bin_str_1[0] and i == "1":
#     result += "0"

# carry = False
# counter = 0
# for i in bin_str_2:
#     print(bin_str_1[counter])
#     counter += 1
#     if carry == True:
#         do something here
#     if i == bin_str_1[0] and i == "1":
#         result += "0"
#         carry = True
#     elif i in bin_str_1 == n in bin_str_2 and i == "0":
#         result += "0"
#     elif (
#         bin_str_1 == "1"
#         and bin_str_2 == "0"
#         or bin_str_1 == "0"
#         and bin_str_2 == "1"
#     ):
#         result += "1"
# return result


# str_1 = "01001"
# str_2 = "10010"
# 11001
# 11

# def dec_bin_convert(dec_num):

#     if not dec_num in range(0, 256):
#         return f"Not in range"
#     binary_number = ""
#     list_of_bits = [128, 64, 32, 16, 8, 4, 2, 1]
#     for bit in list_of_bits:
#         if dec_num >= bit:
#             binary_number += "1"
#             dec_num -= bit
#         else:
#             binary_number += "0"

#     return binary_number


# user_input = int(input("Please enter a number between 0 to 255: "))

# print(dec_bin_convert(user_input))
# # ******************************************************************************************************
# # ******************************************************************************************************
def bin_dec_convert(bin_str):
    base_int = 0
    bit_val = 128
    if len(bin_str) != 8:
        return "That is not a valid number"
    for num in bin_str:
       
        if num == "1":
            base_int += bit_val

       
        bit_val = int(bit_val / 2)
    return base_int


# user_bin_input = input("Please enter a 8 bit binary number: ")
# print(bin_dec_convert(user_bin_input))

# Verify both strings are the same length
# Add some kind of carry logic


# def bin_add(bin_str_1, bin_str_2):
#     result = ""
#     print(bin_str_1)
#     print(bin_str_2)
#     for index, i in enumerate(bin_str_2):
#         if i == bin_str_1[index] and i == "1":
#             result += "0"
# elif i in bin_str_1 == n in bin_str_2 and i == "0":
#     result += "0"
# elif (
#     bin_str_1 == "1"
#     and bin_str_2 == "0"
#     or bin_str_1 == "0"
#     and bin_str_2 == "1"
# ):
#     result += "1"
# return result


# str_1 = "01001"
# str_2 = "10010"
