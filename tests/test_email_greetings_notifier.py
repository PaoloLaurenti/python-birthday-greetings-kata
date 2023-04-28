from datetime import date
from greeter.greeting import Greeting
from greeter.greetings.emails.email import Email
from greeter.greetings.emails.email_greetings_notifier import EmailGreetingsNotifier
from tests.support.fake_mailer import FakeMailer


class TestEmailGreetingsNotifier:
    def test_greet_one_friend(self):
        mailer = FakeMailer()
        notifier = EmailGreetingsNotifier(
            email_from="greeter@kata.com", mailer=mailer
        )
        greetings = [
            Greeting(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
            )
        ]
        notifier.notify(greetings)

        emails = mailer.get_sent_emails()
        assert len(emails) == 1
        assert emails[0] == Email(
            from_address="greeter@kata.com",
            to_address="franco@franchi.com",
            subject="Happy birthday Franco Franchi!",
            text_body="Dear Franco Franchi, happy birthday.",
        )
