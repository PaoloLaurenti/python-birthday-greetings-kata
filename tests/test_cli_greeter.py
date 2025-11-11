import sys
from birthday_greeter.cli.birthday_greeter_config import BirthdayGreeterConfig
from birthday_greeter.cli.cli_greeter import CliGreeter
from tests.support.greeter_test_double import GreeterTestDouble


class TestEmailGreetingsNotifier:
    def test_run_greeter_printing_execution_output(self, capsys):
        greeter_spy = GreeterTestDouble()

        cli = CliGreeter()
        result = cli.run(greeter_spy)

        assert result == 0
        run_calls = greeter_spy.spied_run_calls()
        assert run_calls == 1
        captured = capsys.readouterr()
        assert (
            captured.out == "Sending birthday greetings...\nBirthday Greetings sent.\n"
        )

    def test_parse_input_arguments(self, monkeypatch):
        monkeypatch.setattr(
            sys,
            "argv",
            [
                "birthday_greeter.py",
                "-f",
                "/temp/friends.txt",
                "-m",
                "sender@email.com",
                "-s",
                "+393334445551",
            ],
        )
        cli_greeter = CliGreeter()
        actual_config = cli_greeter.get_config()

        assert actual_config == BirthdayGreeterConfig(
            friends_file_path="/temp/friends.txt",
            email_sender="sender@email.com",
            sms_sender="+393334445551",
        )
