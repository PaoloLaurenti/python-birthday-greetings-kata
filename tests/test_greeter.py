from datetime import date
from greeter.friend import Friend
from greeter.greeter import Greeter
from greeter.greeting import Greeting
from tests.support.clock_test_double import ClockTestDouble
from tests.support.friends_gateway_test_double import FriendsGatewayTestDouble
from tests.support.greetings_notifier_spy import GreetingsNotifierSpy


class TestGreeter:
    def test_greets_many_friends_on_their_birthdays(self):
        friends_gateway_test_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
            ),
            Friend(
                name="Luciana Luciani",
                email="luciana@luciani.com",
                birthday=date(1980, 4, 22),
            ),
        ]
        friends_gateway_test_double.stub_friends(stubbed_friends)
        clock_test_double = ClockTestDouble()
        clock_test_double.stub_local_tz_today(date(2023, 4, 22))
        greetings_notifier_test_double = GreetingsNotifierSpy()
        greeter = Greeter(friends_gateway_test_double, clock_test_double, greetings_notifier_test_double)

        greeter.send_greetings()

        notified_greetings = greetings_notifier_test_double.get_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1974, 4, 22),
        )
        expected_greeting_2 = Greeting(
            name="Luciana Luciani",
            email="luciana@luciani.com",
            birthday=date(1980, 4, 22),
        )
        assert len(notified_greetings) == 2
        assert notified_greetings[0] == expected_greeting_1
        assert notified_greetings[1] == expected_greeting_2
