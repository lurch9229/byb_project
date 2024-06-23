# --- OOP Email Simulator --- #

#  Create class Email with parameters for
#  email address, subject line and email contents
class Email:

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True  # Add method to mark email as read on open


inbox = []


def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    inbox.append(Email("abc@123.net", "Hello", "Hello, how are you?"))
    inbox.append(Email("xyz@aol.com", "Apples", "Do you like apples?"))
    inbox.append(Email("jeeves@yahoo.com", "Throwback", "Did you ever use AskJeeves"))


def list_emails():
    for i, inbox_list in enumerate(inbox):  # Assign objects in list a key during iteration
        print(f"\nSubject: {inbox_list.subject_line}\nInbox ID: {i}\n")


def read_email(index):
    email_display = inbox[index]  # Get index of inbox and display all data from each email
    print(f"Email Address: {email_display.email_address}"
          f"\nSubject: {email_display.subject_line}"
          f"\nEmail Content: {email_display.email_content}\n")
    email_display.mark_as_read()  # When email is viewed read status changes to true


populate_inbox()

while True:

    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:

        list_emails()
        email_choice = int(input("Which email would you like to read? Enter the ID of the email"))

        if len(inbox) < email_choice < 0:
            print(f"Email ID does not exist")
        else:
            print("Reading Email\n ")
            read_email(email_choice)
    elif user_choice == 2:
        for item, email in enumerate(inbox):  # Used to determine if an email has already been read
            if not email.has_been_read:
                read_email(item)
        print("No unread emails")

    elif user_choice == 3:
        print("Closing program")
        break

    else:
        print("Oops - incorrect input.")
        break
