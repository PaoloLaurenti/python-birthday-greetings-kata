import sys

from birthday_greeter.cli.cli_greeter import CliGreeter
from birthday_greeter.friends.flat_file.flat_file_friends_gateway import (
    FlatFileFriendsGateway,
)
from birthday_greeter.greeter_engine import GreeterEngine
from birthday_greeter.greetings.emails.email_greetings_notifier import (
    EmailGreetingsNotifier,
)
from birthday_greeter.greetings.emails.mailer import Mailer
from birthday_greeter.greetings.greetings_notifier_announcer import (
    GreetingsNotifierAnnouncer,
)
from birthday_greeter.greetings.logs.greetings_notifier_logger import (
    GreetingsNotifierLogger,
)
from birthday_greeter.greetings.sms.sms_greetings_notifier import SmsGreetingsNotifier
from birthday_greeter.greetings.sms.sms_service import SmsService
from birthday_greeter.time.clock import Clock


class RealMailer(Mailer):
    def send(self, _email):
        raise NotImplementedError


class RealSmsService(SmsService):
    def send(self, sms):
        raise NotImplementedError


def main():
    cli_greeter = CliGreeter()
    greeter_config = cli_greeter.get_config()
    friends_gateway = FlatFileFriendsGateway(greeter_config.friends_file_path)
    clock = Clock()
    mailer = RealMailer()
    email_greetings_notifier = EmailGreetingsNotifier(
        email_from=greeter_config.email_sender, mailer=mailer
    )
    sms_service = RealSmsService()
    sms_greetings_notifier = SmsGreetingsNotifier(
        from_phone_number=greeter_config.sms_sender, sms_service=sms_service
    )
    greetings_notifier_announcer = GreetingsNotifierAnnouncer(
        [email_greetings_notifier, sms_greetings_notifier]
    )
    greetings_notifier_logger = GreetingsNotifierLogger(greetings_notifier_announcer)

    greeter_engine = GreeterEngine(friends_gateway, clock, greetings_notifier_logger)

    cli_greeter.run(greeter_engine)
    return 0


if __name__ == "__main__":
    sys.exit(main())
