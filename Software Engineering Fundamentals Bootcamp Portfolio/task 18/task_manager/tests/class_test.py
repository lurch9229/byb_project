import unittest
from unittest.mock import patch
from src.models.user import User
from src.models.task import Task


class TestUser(unittest.TestCase):
    def test_create_new_user_matching_passwords(self):
        with patch("builtins.input", side_effect=["testuser", "password", "password"]):
            new_user = User.create_new_user(role="User")
            self.assertIsInstance(new_user, User)
            self.assertEqual(new_user.username, "testuser")
            self.assertEqual(new_user.role, "User")

    def test_create_new_user_non_matching_passwords(self):
        with patch("builtins.input", side_effect=["testuser", "password1", "password2"]):
            new_user = User.create_new_user(role="User")
            self.assertIsNone(new_user)


class TestTask(unittest.TestCase):
    def test_mark_completed(self):
        task = Task(title="Sample Task", description="This is a test task")
        task.mark_completed()
        self.assertEqual(task.status, "Finished")

    def test_from_string(self):
        task_string = "42, Example Task, Do something important, True"
        task = Task.from_string(task_string)
        self.assertIsInstance(task, Task)
        self.assertEqual(task.task_id, 42)
        self.assertEqual(task.title, "Example Task")
        self.assertEqual(task.description, "Do something important")
        self.assertEqual(task.status, "Finished")


if __name__ == "__main__":
    unittest.main()
