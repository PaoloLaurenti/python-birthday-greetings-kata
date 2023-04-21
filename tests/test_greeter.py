from datetime import date
from greeter.friend import Friend
from greeter.greeter import Greeter
from greeter.greeting import Greeting
from tests.support.friends_gateway_test_double import FriendsGatewayTestDouble
from tests.support.greetings_notifier_spy import GreetingsNotifierSpy

class TestGreeter:
    def test_greets_many_friends_on_their_birthdays(self):
        friends_gateway = FriendsGatewayTestDouble()
        greetings_notifier = GreetingsNotifierSpy()
        greeter = Greeter(friends_gateway, greetings_notifier)
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 6, 24),
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
            ),
        ]
        friends_gateway.stub_friends(stubbed_friends)

        greeter.send_greetings()

        notified_greetings = greetings_notifier.get_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1974, 6, 24),
        )
        expected_greeting_2 = Greeting(
            name="Marco Marchi",
            email="marco@marchi.com",
            birthday=date(1980, 5, 11),
        )
        assert len(notified_greetings) == 2
        assert notified_greetings[0] == expected_greeting_1
        assert notified_greetings[1] == expected_greeting_2
