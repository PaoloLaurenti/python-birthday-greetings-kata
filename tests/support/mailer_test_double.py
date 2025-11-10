from birthday_greeter.greetings.emails.mailer import Mailer


class MailerTestDouble(Mailer):
    def __init__(self):
        self.sent_emails = []

    def send(self, email):
        self.sent_emails.append(email)

    def get_spied_sent_emails(self):
        return self.sent_emails
