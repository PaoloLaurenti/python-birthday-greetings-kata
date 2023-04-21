import os
from datetime import date

from greeter.greeter import Greeter
from greeter.greeting import Greeting
from tests.support.greetings_notifier_spy import GreetingsNotifierSpy


class TestGreeter:
    def test_greets_one_friend_on_his_birthday(self):
        greetings_notifier = GreetingsNotifierSpy()
        greeter = Greeter(greetings_notifier)

        greeter.send_greetings()

        notified_greetings = greetings_notifier.get_notified_greetings()
        expected_greeting = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1974, 6, 24),
        )
        assert len(notified_greetings) == 1
        assert notified_greetings[0] == expected_greeting
