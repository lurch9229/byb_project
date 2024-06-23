"""
Enter a list of numbers, finish by typing -1
the average of your entered number will be displayed
"""

# create an empty list for user inputs above -1
user_list = []

# while user inputted number is greater than -1
# place inputted number into user_list
# if -1 is entered first and user list empty, break loop
# end the while loop once -1 is inputted and user_list not empty

while True:
    num = int(input("Please enter a number, -1 will end the program: "))
    if num >= 0:
        user_list.append(int(num))
    elif num == -1:
        """determine if the user_list is empty"""
        if not user_list:
            print("No numbers entered")
            break
        else:
            """take the average/mean of user_list integers and print"""
            average = sum(user_list) / len(user_list)
            print(f"\n{user_list}\nThe average of user inputted numbers is {average}")
            break


#   Added a second if/else statement dependent on if
#   user_list is empty, then stop the program
