"""
program to allow user to input
student information for an exam
"""

"""
get user input for amount of students
create loop for # of students
    each loop ask for student ID
    write IDs to file reg_form.txt
    add dotted line after each ID for signature
"""
file = open("reg_form.txt", "w+")
#   get # of students
student_num = input("Please input number of students attending the exam: ")

#   exception for if # of students isn't an integer
if not student_num != int:
    print("Error. You didn't enter a number")
    student_num = input("Please input number of students attending the exam: ")
else:
    student_num = int(student_num)


for i in range(student_num):
    student_id = input("Please enter a students ID: ")
    file.write(student_id)
    file.write(":       ................\n")
