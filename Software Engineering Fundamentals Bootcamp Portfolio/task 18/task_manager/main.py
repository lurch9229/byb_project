"""
Start point of application. Logs in user as logged_user
Load tasks from file
Displays menu with choices dependent on users role
Takes users choice to display tasks, add task etc
"""

from data.data_access import TaskHandler
from models.menu import Menu


def main():
    # Initialize variables for any loop for pre-initialization
    task_handler = TaskHandler()
    menu = Menu(task_handler)

    while True:
        # menu.login()
        menu.log_in_user()

        if menu.logged_in_user is None:
            break

        # task_handler.load_tasks()

        while True:
            menu.display_menu()
            menu.user_choice()


if __name__ == "__main__":
    main()
