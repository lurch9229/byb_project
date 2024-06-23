import unittest

"""
Testing the display tasks function
"""

tasks = ["Task 1", "Task 2", "Task 3"]


def display_tasks():
    for task in tasks:
        print(task)


class TestDisplayTasks(unittest.TestCase):
    def test_display_tasks(self):
        # Redirect stdout to capture printed output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Call the display_tasks function
        display_tasks()

        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Assert that each task is present in the output
        for task in tasks:
            self.assertIn(task, printed_output)

        # Clean up: restore original stdout
        sys.stdout = original_stdout


"""
Testing the display menu function
"""


def display_menu(logged_user):
    if logged_user == str('User'):
        print("1. View all tasks")
        print("2. View specific task")
        print("3. Exit")


class TestDisplayMenu(unittest.TestCase):
    def test_display_menu_user(self):
        # Create a sample User with 'User' role
        user = str("User")

        import sys
        from io import StringIO

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Call the display_menu function
        display_menu(user)

        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Assert that the correct menu options are present
        self.assertIn("1. View all tasks", printed_output)
        self.assertIn("2. View specific task", printed_output)
        self.assertIn("3. Exit", printed_output)

        # Clean up: restore original stdout
        sys.stdout = original_stdout


if __name__ == "__main__":
    unittest.main()
