from datetime import date
from greeter.greetings.greeting import Greeting
from greeter.greetings.emails.email import Email
from greeter.greetings.emails.email_greetings_notifier import EmailGreetingsNotifier
from tests.support.mailer_test_double import MailerTestDouble


class TestEmailGreetingsNotifier:
    def test_greet_many_friends(self):
        mailer_double = MailerTestDouble()
        notifier = EmailGreetingsNotifier(
            email_from="greeter@kata.com", mailer=mailer_double
        )
        greetings = [
            Greeting(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
            ),
            Greeting(
                name="Luciana Luciani",
                email="luciana@luciani.com",
                birthday=date(1980, 4, 22),
            ),
        ]
        notifier.notify(greetings)

        emails = mailer_double.get_spied_sent_emails()
        assert emails == [
            Email(
                from_address="greeter@kata.com",
                to_address="franco@franchi.com",
                subject="Happy birthday Franco Franchi!",
                text_body="Dear Franco Franchi, happy birthday.",
            ),
            Email(
                from_address="greeter@kata.com",
                to_address="luciana@luciani.com",
                subject="Happy birthday Luciana Luciani!",
                text_body="Dear Luciana Luciani, happy birthday.",
            ),
        ]
