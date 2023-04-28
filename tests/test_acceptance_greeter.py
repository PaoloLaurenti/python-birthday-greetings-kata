from datetime import date
import tempfile
from greeter.friends.flat_file_friends_gateway import FlatFileFriendsGateway
from greeter.greeter import Greeter
from greeter.greetings.emails.email import Email
from greeter.greetings.emails.email_greetings_notifier import EmailGreetingsNotifier
from tests.support.fake_immutable_clock import FakeImmutableClock
from tests.support.fake_mailer import FakeMailer


class TestAcceptanceGreeter:
    def test_send_greetings_to_friends(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.writelines(
                [
                    b"last_name, first_name, date_of_birth, email\n",
                    b"Franchi, Franco, 1974/04/22, franco@franchi.com\n",
                    b"Maura, Mauri, 1998/08/02, mauro@mauri.com\n",
                    b"Luciani, Luciana, 1980/04/22, luciana@luciani.com\n",
                ]
            )
            tmp.seek(0)

            friends_gateway = FlatFileFriendsGateway(tmp.name)
            clock = FakeImmutableClock(date(2023, 4, 22))
            mailer = FakeMailer()
            greetings_notifier = EmailGreetingsNotifier(
                email_from="greeter@kata.com", mailer=mailer
            )

            greeter = Greeter(friends_gateway, clock, greetings_notifier)

            greeter.send_greetings()

            emails = mailer.get_sent_emails()
            assert len(emails) == 2
            assert emails[0] == Email(
                from_address="greeter@kata.com",
                to_address="franco@franchi.com",
                subject="Happy birthday Franco Franchi!",
                text_body="Dear Franco Franchi, happy birthday.",
            )
            assert emails[1] == Email(
                from_address="greeter@kata.com",
                to_address="luciana@luciani.com",
                subject="Happy birthday Luciana Luciani!",
                text_body="Dear Luciana Luciani, happy birthday.",
            )