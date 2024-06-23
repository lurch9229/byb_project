"""
Create the following variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

convert num1 from an FLOAT to an INT (whole number)
convert num2 from an INT to a FLOAT (decimal number)
convert num3 from an INT to a STRING (text)
convert string1 from a STRING to an INT (whole number)
"""

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

print(num1)
print("num1 is a ", type(num1), "type")
print(num2)
print("num2 is a ", type(num2), "type")
print(num3)
print("num3 is a ", type(num3), "type")
print(string1)
print("string1 is a ", type(string1), "type")

# convert float to int

new_num1 = int(num1)
print(new_num1)
print("new_num1 is a ", type(new_num1), "type")

# convert int to float

new_num2 = float(num2)
print(new_num2)
print("new_num2 is a ", type(new_num2), "type")

# convert int to string

new_num3 = str(num3)
print(new_num2)
print("new_num3 is a ", type(new_num3), "type")

# convert string to int

new_string1 = int(string1)
print(new_string1)
print("new_string1 is a ", type(new_string1), "type")
