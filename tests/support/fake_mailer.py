from greeter.greetings.emails.mailer import Mailer


class FakeMailer(Mailer):
    def __init__(self):
        self.sent_emails = []

    def send(self, email):
        self.sent_emails.append(email)

    def get_sent_emails(self):
        return self.sent_emails
