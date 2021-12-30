# Question 2
# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

# def is_even(k):
#
#     x = bin(k)
#     if x[len(x)-1] == '0':
#         return True
#     else:
#         return False
#
#
# print(is_even())

def is_even(k):  # Defining a function which is finding if a given number is even or odd
    if k & 1 == 0:  # LSB (binary) of input == 0 then even, otherwise odd
        return True   # Returning True if LSB of 'k' == 0
    else:
        return False  # Returning False


print(is_even(11))   # Calling & getting bool answer
