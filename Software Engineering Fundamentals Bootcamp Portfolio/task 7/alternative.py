"""
Alternate cases per letter

create variables

take input from alt and get the character length
    loop through char length
    if index can not be divided by 2
        make index upper case
        add to alt_final string
    else
        make index lower case
        add to alt_final string
"""

# create variables
alt = input("Enter a sentence: ")
char_len = len(alt)
alt_final = ""

#   for loop that will iterate number of times determined
#   by the char_len

for i in range(char_len):
    if not i % 2:   # check if the index is divisible by 2
        alt_final = alt_final + alt[i].upper()
    else:
        alt_final = alt_final + alt[i].lower()


print(f'\nYou entered "{alt}".\nAlternating cap letters are: "{alt_final}"')

"""
Alternate cases per word

create variables

take input from alt and split words
    loop through word length
    if can be divided by 2
        make index uppercase
        add to list
        join into string
    else
        make index lowercase
        add to list
        join into string    
"""

#   create variables

alt_split = alt.split()
word_len = len(alt_split)
word_final = []
word_result = ""

#   loop indexes in word_len
for i in range(word_len):
    if not i % 2:
        c_upper = alt_split[i].upper()  # split word on odd index and make it upper case
        # print(alt_split[i].upper())
        word_final.append(c_upper)  # add upper case word to list
        word_result = " ".join(word_final)  # join list to make a string
    else:
        c_lower = alt_split[i].lower()  # split word on even index and make it lower case
        # print(alt_split[i].lower())
        word_final.append(c_lower)  # add lower case word to list
        word_result = " ".join(word_final)  # join list to make string


# print(word_final)
print(f'\nYou entered "{alt}".\nAlternating cap words are: "{word_result}"')
