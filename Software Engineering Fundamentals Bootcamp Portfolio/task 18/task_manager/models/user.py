import hashlib
import os
from abc import ABC
from data import TaskHandler


class BaseUser(ABC):

    def print_menu(self):
        pass

    def input_menu(self, choice, menu):
        pass

    def change_role(self, role_to_be):
        pass


class User(BaseUser):
    def __init__(self, username, task_handler: TaskHandler, role="User"):
        self.task_handler = task_handler
        self.username = username
        self.role = role

    def print_menu(self):
        print("1. View all tasks\n"
              "2. View specific task\n"
              "3. Add Task\n"
              "4. Exit")

    def input_menu(self, choice, menu):
        """
        Takes users choice to display tasks or add tasks
        """
        if choice == 1:
            try:
                self.task_handler.display_tasks()  # Display all tasks

            except FileNotFoundError:
                print("No Tasks File")

        elif choice == 2:
            while True:
                try:
                    task_id = int(
                        input("Please enter a Task ID. 0 will quit back to menu: ")
                    )
                    if task_id == 0:
                        break
                    else:
                        task = self.task_handler.load_task_by_id(task_id)  # Display a task by ID

                    if task:
                        print(task)

                    else:
                        print("Task Not Found")

                except ValueError:
                    print("Invalid input.")

        elif choice == 3:
            self.task_handler.create_new_task()  # Create a new task to add to the tasks.txt

        elif choice == 4:
            print("Logging Out..")
            menu.log_in_user()

        else:
            print("Input Error. Please enter a number in range")

    @classmethod
    def create_new_user(cls, role="User"):
        username = input("Enter a Username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if confirm_password == password:
            enc = confirm_password.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            file_path = os.path.join(
                os.path.dirname(__file__), "..", "data", "credentials.txt"
            )
            with open(file_path, "a") as f:
                f.write(f"{username}, {hash1}, {role}\n")
            print("You have registered successfully!")
            return cls(username, TaskHandler(), role="User")
        else:
            print("Passwords do not match!.\n")


class Moderator(User):
    def __init__(self, username, task_handler: TaskHandler, role="Moderator"):
        super().__init__(username, task_handler, role)
        # self.role = "Moderator"

    def print_menu(self):
        print(
            "1. View all tasks\n"
            "2. View specific task\n"
            "3. Add a task\n"
            "4. Update a task\n"
            "5. Exit"
        )

    def input_menu(self, choice, menu):
        """
        Takes moderators choice to display, add or update tasks
        """
        if choice == 1:
            try:
                self.task_handler.display_tasks()  # Displays all tasks

            except FileNotFoundError:
                print("No Tasks Found")

        elif choice == 2:
            while True:
                try:
                    task_id = int(
                        input("Please enter a Task ID. 0 will quit back to menu: ")
                    )
                    if task_id == 0:
                        return

                    else:
                        task = self.task_handler.load_task_by_id(task_id)  # Displays a task based on ID

                    if task:
                        print(task)

                except ValueError:
                    print("Invalid Input.")

        elif choice == 3:
            self.task_handler.create_new_task()  # Create a new task

        # Edit a task using update_task() and a task ID
        elif choice == 4:
            """
            Update a task based on its ID. Can update a tasks Title, Description and Status
            """
            try:
                task_id = int(input("Enter task ID to edit. Use 0 to go back: "))
                if task_id == 0:
                    return

                else:
                    self.task_handler.update_task(task_id)
                    print(f"Task {task.task_id} Updated")

            except ValueError:
                print("Invalid Input. Please enter a valid Task ID")

        elif choice == 5:
            print("Logging Out..")
            menu.log_in_user()  # Break out of the menu and return to log in

        else:
            print("Input Error. Please enter a number in range")


class Admin(User):
    def __init__(self, username, task_handler: TaskHandler, role="Admin"):
        super().__init__(username, task_handler, role)

    # def __init__(self, username):
    #     super().__init__(username)
    #     self.role = "Admin"

    def assign_moderator(self, target_username, file_path):
        """Assigns moderator permissions to the user with the given name."""
        updated_lines = []
        try:
            with open(file_path, "r") as f:
                for line in f:
                    stored_username, stored_hash, stored_role = line.strip().split(", ")
                    if stored_username == target_username:
                        updated_lines.append(
                            f"{stored_username}, {stored_hash}, Moderator\n"
                        )
                        print(f"{target_username} has been promoted to Moderator.")
                    else:
                        updated_lines.append(line)

            # Write the updated content back to the file
            with open(file_path, "w") as f:
                f.writelines(updated_lines)
        except FileNotFoundError:
            print("User credentials file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def print_menu(self):
        print(
            "1. View all tasks\n"
            "2. View specific task\n"
            "3. Add a new task\n"
            "4. Update a task\n"
            "5. Delete a task\n"
            "6. View users\n"
            "7. Give user Moderator role\n"
            "8. Exit"
        )

    def input_menu(self, choice, menu):
        """
        Takes admin input to display, add, updated and delete tasks
        Can also view users and give moderator role
        """
        if choice == 1:
            try:
                self.task_handler.display_tasks()

            except FileNotFoundError:
                print("No Tasks Found")

        elif choice == 2:
            while True:
                try:
                    task_id = int(
                        input("Please enter a Task ID. 0 will quit back to menu: ")
                    )
                    if task_id == 0:
                        break
                    else:
                        task = self.task_handler.load_task_by_id(task_id)

                    if task:
                        print(task)

                except ValueError:
                    print("Invalid Input.")

        # Create a new task. ID and status are handled by the Task class
        # Takes a title and decsription to create a new task
        elif choice == 3:
            self.task_handler.create_new_task()

        elif choice == 4:
            try:
                task_id = int(input("Enter task ID to edit. Use 0 to go back: "))
                if task_id == 0:
                    return

                else:
                    self.task_handler.update_task(task_id)
                    print(f"Task {task.task_id} Updated")

            except ValueError:
                print("Invalid Input. Please enter a valid Task ID")

        elif choice == 5:
            try:
                task_id = int(input("Enter task ID to delete. Use / to go back: "))
                if task_id == "/":
                    return

                else:
                    self.task_handler.delete_task(task_id)  # Delete a task based on ID

            except ValueError:
                print("Invalid ID. Please enter a valid Task ID")

        elif choice == 6:
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "credentials.txt")
            try:
                with open(file_path, "r") as f:
                    for line in f:
                        stored_username, _, stored_role = line.strip().split(", ")
                        print(f"Username: {stored_username}, Role: {stored_role}")  # Displays all users

            except FileNotFoundError:
                print("User credentials file not found.")

        # Give a User the Moderator role
        elif choice == 7:
            file_path = os.path.join(os.path.dirname(__file__), "..", "data", "credentials.txt")

            # file_path = os.path.join(os.path.dirname(__file__), "credentials.txt")

            try:
                with open(file_path, "r") as file:
                    for line in file:
                        stored_username, _, stored_role = line.strip().split(", ")
                        print(f"Username: {stored_username}, Role: {stored_role}")

            except FileNotFoundError:
                print("User credentials file not found.")

            new_mod = input("Please enter the name of the user you want to promote. Use / to go back: ")
            if new_mod == "/":
                return

            else:
                Admin(new_mod, TaskHandler()).assign_moderator(new_mod, file_path)  # Change a users role to Moderator

        elif choice == 8:
            print("Logging Out..")
            menu.log_in_user()

        else:
            print("Input Error. Please enter a number in range")
