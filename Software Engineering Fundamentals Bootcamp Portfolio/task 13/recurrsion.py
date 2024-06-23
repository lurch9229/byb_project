# Factorial of 5 is
# 5! = 5 x (5 - 1)
# n! = n x (n -1)
# 5 x 4 x 3 x 2 x (0)!

def factorial(number):
    if number == 0:
        return 1  # Base Case
    else:  # This else is redundant, need to look into why it is not needed
        value = number * factorial(number - 1)  # New argument and where loop occurs due to the function calling itself
        return value  #


print(factorial(5))

# BASE CASE - function returns a value when a certain condition is met, without any other recursive call
# RECURSIVE CALL -


# # # force a stack overflow for recursion # # #

# def factorial(number):
#     value = number + factorial(number - 1)
#     return value
#
#
# print(factorial(5))


# class Product:
#
#     def __init__(self):
#         pass
#
#     def product(self, a, b):
#         return a + (self.product(3, b -1))
#
#     def product_normal(self, a, b):
#         return a + b
#
#     def product_iterative(self, a, b):
#         pass
#

# def cut_cake(num_friends, num_slices):
#     # Cut cake in half
#     num_slices = num_slices * 2
#     # Check if there are enough slices
#     if num_slices >= num_friends:
#         # If there are enough slices return the number of slices
#         return num_slices
#     else:
#         # If there is not enough slices
#         # Cut in half again
#         return cut_cake(num_friends, num_slices)
#
#
# print(cut_cake(11, 1))


# 1st function call - cut_cake(11, 1) - new num_slices value is passed
# as an argument in the next recursive function call (num_slices = 2) and
# num_friends = 11 because num_friends stays consistent

# 2nd function call because num_slices < num_friends after previous function call - cut_cake(11,2)
# . New num_slices value is passed as an argument in the next recursive
# function call(num_slices = 4) and num_friends = 11

# 3rd function call because num_slices < num_friends - cut_cake(11,4)
# New num_slices passes as an argument in the next function call
# num_slices = 8 and num_friends = 11

# 4th function call because num_slices < num_friends - cut_cake(11,8)
# New num_slices = 16 is returned because base class is met (num_slices > num_friends)
# Recursion has ended and value printed is 16


