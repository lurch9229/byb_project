"""
Reads from a file and separates name and DOB into
2 different string lists
"""
"""
open file
for each line in opened file
    get length of words in each line
    split line into [0,1] and [2,4] lists
    make the lists into a string
        remove/replace any special characters
        be sure each object is on a new line
"""
#   create variables and open file
file = open('DOB.txt', 'r', encoding='utf-8-sig')
name = ""
dob = ""
char_remove = [",", "'", "["]


for i in file:  # read each line in file
    e = i.split()[0:2]  # get first 2 words for name
    o = i.split()[2:5]  # get next 3 words for dob
    name_split = str(e)  # add names to string
    dob_split = str(o)  # add dates to string
    name_split = name_split.replace("]", "\n")  # replace last special character with \n
    dob_split = dob_split.replace("]", "\n")
    for x in name_split:    # loop through current names
        if x not in char_remove:    # remove special characters
            name += x

    for x in dob_split:   # loop through current dates
        if x not in char_remove:    # remove special characters
            dob += x


print(f"Name:\n{name}")
print(f"Date of Birth:\n{dob}")
