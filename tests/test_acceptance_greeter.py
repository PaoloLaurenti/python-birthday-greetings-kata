from datetime import date
import tempfile
from greeter.friends.flat_file_friends_gateway import FlatFileFriendsGateway
from greeter.greeter import Greeter
from greeter.greetings.emails.email import Email
from greeter.greetings.emails.email_greetings_notifier import EmailGreetingsNotifier
from greeter.greetings.greetings_notifier_announcer import GreetingsNotifierAnnouncer
from greeter.greetings.sms.sms import Sms
from greeter.greetings.sms.sms_greetings_notifier import SmsGreetingsNotifier
from tests.support.fake_immutable_clock import FakeImmutableClock
from tests.support.fake_mailer import FakeMailer
from tests.support.sms_service_test_double import SmsServiceTestDouble


class TestAcceptanceGreeter:
    def test_send_greetings_to_friends(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.writelines(
                [
                    b"last_name, first_name, date_of_birth, email, sms\n",
                    b"Franchi, Franco, 1974/04/22, franco@franchi.com, 3338889991\n",
                    b"Maura, Mauri, 1998/08/02, mauro@mauri.com, 3356669998\n",
                    b"Luciani, Luciana, 1980/04/22, luciana@luciani.com, 3337776662\n",
                ]
            )
            tmp.seek(0)

            friends_gateway = FlatFileFriendsGateway(tmp.name)
            clock = FakeImmutableClock(date(2023, 4, 22))
            mailer = FakeMailer()
            email_greetings_notifier = EmailGreetingsNotifier(
                email_from="greeter@kata.com", mailer=mailer
            )
            sms_service_spy = SmsServiceTestDouble()
            sms_greetings_notifier = SmsGreetingsNotifier(
                from_phone_number="3225554447", sms_service=sms_service_spy
            )
            greetings_notifier_announcer = GreetingsNotifierAnnouncer([email_greetings_notifier, sms_greetings_notifier])

            greeter = Greeter(friends_gateway, clock, greetings_notifier_announcer)

            greeter.send_greetings()

            emails = mailer.get_sent_emails()
            sms = sms_service_spy.get_sent_sms()
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
            assert sms == [
                Sms(
                    from_phone_number="3225554447",
                    to_phone_number="3338889991",
                    text="Happy birthday Franco Franchi!",
                ),
                Sms(
                    from_phone_number="3225554447",
                    to_phone_number="3337776662",
                    text="Happy birthday Luciana Luciani!",
                ),
            ]
