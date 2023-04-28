from greeter.greetings.emails.email import Email
from greeter.greetings.greetings_notifier import GreetingsNotifier


class EmailGreetingsNotifier(GreetingsNotifier):
    def __init__(self, email_from, mailer):
        self.email_from = email_from
        self.mailer = mailer

    def notify(self, greetings):
        emails = map(lambda g: self.greeting_to_email(g), greetings)
        for email in emails:
            self.mailer.send(email)

    def greeting_to_email(self, greeting):
        subject = f"Happy birthday {greeting.name}!"
        text_body = f"Dear {greeting.name}, happy birthday."
        return Email(
            from_address=self.email_from,
            to_address=greeting.email,
            subject=subject,
            text_body=text_body,
        )
