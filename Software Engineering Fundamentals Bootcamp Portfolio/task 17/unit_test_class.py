import unittest
import email


class TestEmail(unittest.TestCase):

    def setUp(self):
        # Ran before every individual unit test. Makes Email object we  use in testing
        self.email = email.Email("test@email.com", "Test Subject", "This is an email for unit testing")
    
    def test_init(self):
        # Tests the initialisation for the Email object
        self.assertEqual(self.email.email_address, "test@email.com")
        self.assertEqual(self.email.subject_line, "Test Subject")
        self.assertEqual(self.email.email_content, "This is an email for unit testing")
        self.assertFalse(self.email.has_been_read)
    
    def test_mark_as_read(self):
        # Test if method correctly marks email as read
        self.email.mark_as_read()
        self.assertTrue(self.email.has_been_read)


if __name__ == "__main__":
    unittest.main()
    