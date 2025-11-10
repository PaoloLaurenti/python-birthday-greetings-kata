from birthday_greeter.cli.cli_greeter import CliGreeter
from tests.support.greeter_test_double import GreeterTestDouble


class TestEmailGreetingsNotifier:
    def test_run_greeter_printing_execution_output(self, capsys):
        greeter_spy = GreeterTestDouble()

        cli_greeter = CliGreeter(greeter_spy)
        result = cli_greeter.run()

        assert result == 0
        run_calls = greeter_spy.spied_run_calls()
        assert run_calls == 1
        captured = capsys.readouterr()
        assert (
            captured.out == "Sending birthday greetings...\nBirthday Greetings sent.\n"
        )
