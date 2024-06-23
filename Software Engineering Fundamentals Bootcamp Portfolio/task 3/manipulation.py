str_manip = input("Please enter a sentence ")

# Length of user sentence

print(len(str_manip))

# Last letter of user sentence

last_letter = str_manip[-1]

# replace all occurrences of last_letter with @

print(str_manip.replace(last_letter, "@"))

# Print last 3 letters of user sentence in reverse order

print(str_manip[-1:-4:-1])

jumble = str_manip[:3] + str_manip[-3:]

print(jumble)

