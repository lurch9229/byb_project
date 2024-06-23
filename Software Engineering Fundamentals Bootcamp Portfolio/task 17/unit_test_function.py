import unittest
from io import StringIO
import sys
from email import Email


"""
From here we are testing Functions rather than Class Methods
"""


def populate_inbox(inbox):
    inbox.append(Email("abc@123.net", "Hello", "Hello, how are you?"))
    inbox.append(Email("xyz@aol.com", "Apples", "Do you like apples?"))
    inbox.append(Email("jeeves@yahoo.com", "Throwback", "Did you ever use AskJeeves"))


def list_emails(inbox):
    for i, inbox_list in enumerate(inbox):
        print(f"\nSubject: {inbox_list.subject_line}\nInbox ID: {i}\n")


def read_email(inbox, index):
    email_display = inbox[index]
    print(f"Email Address: {email_display.email_address}"
          f"\nSubject: {email_display.subject_line}"
          f"\nEmail Content: {email_display.email_content}\n")
    email_display.mark_as_read()


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.inbox = []
        populate_inbox(self.inbox)

    def test_populate(self):
        self.assertEqual(len(self.inbox), 3)
        self.assertEqual(self.inbox[0].email_address, "abc@123.net")
        self.assertEqual(self.inbox[1].subject_line, "Apples")
        self.assertEqual(self.inbox[2].email_content, "Did you ever use AskJeeves")

    def test_list_emails(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            list_emails(self.inbox)
        finally:
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            self.assertIn("Subject: Hello", output)
            self.assertIn("Inbox ID: 0", output)
            self.assertIn("Subject: Apples", output)
            self.assertIn("Inbox ID: 1", output)
            self.assertIn("Subject: Throwback", output)
            self.assertIn("Inbox ID: 2", output)

    def test_read_email(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            read_email(self.inbox, 0)
        finally:
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            self.assertIn("Email Address: abc@123.net", output)
            self.assertIn("Subject: Hello", output)
            self.assertIn("Email Content: Hello, how are you?", output)
            self.assertTrue(self.inbox[0].has_been_read)


if __name__ == "__main__":
    unittest.main()
    