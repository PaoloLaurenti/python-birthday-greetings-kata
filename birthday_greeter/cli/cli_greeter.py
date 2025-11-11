import argparse
from birthday_greeter.cli.birthday_greeter_config import BirthdayGreeterConfig


class CliGreeter:
    def run(self, greeter):
        print("Sending birthday greetings...")
        greeter.run()
        print("Birthday Greetings sent.")
        return 0

    def get_config(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f")
        parser.add_argument("-s")
        parser.add_argument("-m")
        args = parser.parse_args()
        return BirthdayGreeterConfig(
            friends_file_path=args.f,
            email_sender=args.m,
            sms_sender=args.s,
        )
