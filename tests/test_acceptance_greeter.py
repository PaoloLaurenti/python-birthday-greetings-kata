from datetime import date
import tempfile
from birthday_greeter.friends.flat_file.flat_file_friends_gateway import (
    FlatFileFriendsGateway,
)
from birthday_greeter.greeter_engine import GreeterEngine
from birthday_greeter.greetings.emails.email import Email
from birthday_greeter.greetings.emails.email_greetings_notifier import (
    EmailGreetingsNotifier,
)
from birthday_greeter.greetings.greetings_notifier_announcer import (
    GreetingsNotifierAnnouncer,
)
from birthday_greeter.greetings.logs.greetings_notifier_logger import (
    GreetingsNotifierLogger,
)
from birthday_greeter.greetings.sms.sms import Sms
from birthday_greeter.greetings.sms.sms_greetings_notifier import SmsGreetingsNotifier
from tests.support.fake_immutable_clock import FakeImmutableClock
from tests.support.mailer_test_double import MailerTestDouble
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
            immutable_clock = FakeImmutableClock(date(2023, 4, 22))
            mailer_double = MailerTestDouble()
            email_greetings_notifier = EmailGreetingsNotifier(
                email_from="greeter@kata.com", mailer=mailer_double
            )
            sms_service_double = SmsServiceTestDouble()
            sms_greetings_notifier = SmsGreetingsNotifier(
                from_phone_number="3225554447", sms_service=sms_service_double
            )
            greetings_notifier_announcer = GreetingsNotifierAnnouncer(
                [email_greetings_notifier, sms_greetings_notifier]
            )
            greetings_notifier_logger = GreetingsNotifierLogger(
                greetings_notifier_announcer
            )

            greeter_engine = GreeterEngine(
                friends_gateway, immutable_clock, greetings_notifier_logger
            )

            greeter_engine.run()

            emails = mailer_double.get_spied_sent_emails()
            sms = sms_service_double.get_spied_sent_sms()
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
