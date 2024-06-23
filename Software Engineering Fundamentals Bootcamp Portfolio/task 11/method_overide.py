"""
Create a program to show how Class inheritance works
"""


class Adult:
    # Attributes using user input
    name = str(input("Enter name: "))
    age = int(input("Enter age: "))
    eye_colour = str(input("Enter eye colour: "))
    hair_colour = str(input("Enter hair colour: "))

    # Constructor with parameters for each attribute
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # Method to display if user can drive
    def can_drive(self):
        print(f"{self.name} can drive. They are of legal age")


# Class inherits from Adult
class Child(Adult):
    # Method overwrites parent method of same name
    def can_drive(self):
        print(f"{self.name} can not drive. They are not of legal age")


# Function to determine if user input is an Adult or a Child
# Prints the users name and if they can drive or not
if Adult.age >= 18:
    adult = Adult(Adult.name, Adult.age, Adult.eye_colour, Adult.hair_colour)
    adult.can_drive()
else:
    child = Child(Child.name, Child.age, Child.eye_colour, Child.hair_colour)
    child.can_drive()
