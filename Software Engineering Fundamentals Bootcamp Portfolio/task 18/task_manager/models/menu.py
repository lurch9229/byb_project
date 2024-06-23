"""
Handles displaying a menu to user
Takes users choice to handle viewing and adding tasks etc
"""

import hashlib
import os
import sys
from .user import User, Admin, Moderator


class Menu:

    def __init__(self, task_handler):
        self.logged_in_user: User = None
        self.task_handler = task_handler

    def log_in_user(self):
        """
        Program starts by logging in a user or creating a new account.
        We then check what the users role is and display the correct menu
        """
        while True:
            try:
                print("Use # to create a new user. Use / to quit app.")
                username = input("Enter username: ")

                if username == "#":
                    User.create_new_user()

                elif username == "/":
                    print("Exiting app..")
                    sys.exit()

                else:
                    password = input("Enter password: ")
                    auth = password.encode()
                    auth_hash = hashlib.md5(auth).hexdigest()
                    print(os.getcwd())
                    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "credentials.txt")

                    with open(file_path, "r") as f:
                        for line in f:
                            stored_username, stored_pwd, stored_role = (
                                line.strip().split(", ")
                            )

                            if username == stored_username and auth_hash == stored_pwd:
                                print(
                                    f"Logged in successfully as {username} {stored_role}"
                                )

                                if stored_role == "User":
                                    self.logged_in_user = User(
                                        username, self.task_handler, role=stored_role
                                    )
                                elif stored_role == "Moderator":
                                    self.logged_in_user = Moderator(
                                        username, self.task_handler, role=stored_role
                                    )
                                elif stored_role == "Admin":
                                    self.logged_in_user = Admin(
                                        username, self.task_handler, role=stored_role
                                    )

                                return
                        else:
                            print("Login failed! Incorrect username or password\n")

            except Exception as e:
                print(f"An error occurred: {e}. Please try again.\n")

    def display_menu(self):
        """
        Displays the main menu after logging in. The display is determined by
        the users role
        """
        while True:
            self.logged_in_user.print_menu()
            return

    def user_choice(self):
        """
        We take an input to move forward in the program. Different roles have
        different inputs
        """
        try:
            choice = int(input("Choose an option: "))
            self.logged_in_user.input_menu(choice, self)

        except ValueError:
            print("Error. Please enter a number in range")
