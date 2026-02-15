

class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
        print(f"Email from {self.sender} marked as read.")


class Mailbox:
    def __init__(self, owner):
        self.owner = owner
        self.emails = []  

    def receive_email(self, email):
        self.emails.append(email)
        print(f"Email received by {self.owner} from {email.sender} with subject '{email.subject}'")

    def show_unread(self):
        print(f"\nUnread emails in {self.owner}'s mailbox:")
        for email in self.emails:
            if not email.is_read:
                print(f"- From: {email.sender} | Subject: {email.subject}")

    def show_all_emails(self):
        print(f"\nAll emails in {self.owner}'s mailbox:")
        for email in self.emails:
            status = "Read" if email.is_read else "Unread"
            print(f"- From: {email.sender} | Subject: {email.subject} | Status: {status}")

    def send_email(self, email, recipient_mailbox):
        recipient_mailbox.receive_email(email)
        print(f"Email sent from {email.sender} to {email.recipient} with subject '{email.subject}'")




john_mailbox = Mailbox("John")
jane_mailbox = Mailbox("Jane")

email1 = Email("john@gmail.com", "jane@gmail.com", "Meeting", "Hi Jane, let's meet tomorrow.")
email2 = Email("jane@gmail.com", "john@gmail.com", "Re: Meeting", "Hi John, I can't make it.")

john_mailbox.send_email(email1, jane_mailbox)
jane_mailbox.send_email(email2, john_mailbox)

john_mailbox.show_unread()
jane_mailbox.show_unread()

email2.mark_as_read()

john_mailbox.show_all_emails()
jane_mailbox.show_all_emails()
