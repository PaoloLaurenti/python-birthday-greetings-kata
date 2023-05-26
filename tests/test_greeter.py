from datetime import date
from greeter.friends.friend import Friend
from greeter.greeter import Greeter
from greeter.greetings.greeting import Greeting
from tests.support.clock_test_double import ClockTestDouble
from tests.support.friends_gateway_test_double import FriendsGatewayTestDouble
from tests.support.greetings_notifier_test_double import GreetingsNotifierTestDouble


class TestGreeter:
    def test_greets_many_friends_on_their_birthdays(self):
        friends_gateway_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
                phone_number="3331112223"
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
                phone_number="3339998881"
            ),
            Friend(
                name="Luciana Luciani",
                email="luciana@luciani.com",
                birthday=date(1980, 4, 22),
                phone_number="3332223334"
            ),
        ]
        friends_gateway_double.stub_friends(stubbed_friends)
        clock_double = ClockTestDouble()
        clock_double.stub_local_tz_today(date(2023, 4, 22))
        greetings_notifier_double = GreetingsNotifierTestDouble()
        greeter = Greeter(
            friends_gateway_double, clock_double, greetings_notifier_double
        )

        greeter.send_greetings()

        notified_greetings = greetings_notifier_double.get_spied_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1974, 4, 22),
            phone_number="3331112223"
        )
        expected_greeting_2 = Greeting(
            name="Luciana Luciani",
            email="luciana@luciani.com",
            birthday=date(1980, 4, 22),
            phone_number="3332223334"
        )
        assert len(notified_greetings) == 2
        assert notified_greetings[0] == expected_greeting_1
        assert notified_greetings[1] == expected_greeting_2

    def test_no_greets_due_to_no_friends_birthday(self):
        friends_gateway_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
                phone_number="3331112223"
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
                phone_number="3331112223"
            )
        ]
        friends_gateway_double.stub_friends(stubbed_friends)
        clock_double = ClockTestDouble()
        clock_double.stub_local_tz_today(date(2023, 1, 1))
        greetings_notifier_double = GreetingsNotifierTestDouble()
        greeter = Greeter(
            friends_gateway_double, clock_double, greetings_notifier_double
        )

        greeter.send_greetings()

        notified_greetings = greetings_notifier_double.get_spied_notified_greetings()
        assert len(notified_greetings) == 0

    def test_29th_feb_birthday_on_leap_year(self):
        friends_gateway_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1976, 2, 29),
                phone_number="3331112223"
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
                phone_number="3339991114"
            )
        ]
        friends_gateway_double.stub_friends(stubbed_friends)
        clock_double = ClockTestDouble()
        clock_double.stub_local_tz_today(date(2024, 2, 29))
        greetings_notifier_double = GreetingsNotifierTestDouble()
        greeter = Greeter(
            friends_gateway_double, clock_double, greetings_notifier_double
        )

        greeter.send_greetings()

        notified_greetings = greetings_notifier_double.get_spied_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1976, 2, 29),
            phone_number="3331112223"
        )
        assert len(notified_greetings) == 1
        assert notified_greetings[0] == expected_greeting_1

    def test_29th_feb_birthday_on_non_leap_year(self):
        friends_gateway_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1976, 2, 29),
                phone_number="3331112223"
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
                phone_number="3339998884"
            )
        ]
        friends_gateway_double.stub_friends(stubbed_friends)
        clock_double = ClockTestDouble()
        clock_double.stub_local_tz_today(date(2023, 2, 28))
        greetings_notifier_double = GreetingsNotifierTestDouble()
        greeter = Greeter(
            friends_gateway_double, clock_double, greetings_notifier_double
        )

        greeter.send_greetings()

        notified_greetings = greetings_notifier_double.get_spied_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1976, 2, 29),
            phone_number="3331112223"
        )
        assert len(notified_greetings) == 1
        assert notified_greetings[0] == expected_greeting_1

    def test_28th_feb_birthday_on_leap_year(self):
        friends_gateway_double = FriendsGatewayTestDouble()
        stubbed_friends = [
            Friend(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1976, 2, 28),
                phone_number="3331112223"
            ),
            Friend(
                name="Marco Marchi",
                email="marco@marchi.com",
                birthday=date(1980, 5, 11),
                phone_number="3339998884"
            )
        ]
        friends_gateway_double.stub_friends(stubbed_friends)
        clock_double = ClockTestDouble()
        clock_double.stub_local_tz_today(date(2024, 2, 28))
        greetings_notifier_double = GreetingsNotifierTestDouble()
        greeter = Greeter(
            friends_gateway_double, clock_double, greetings_notifier_double
        )

        greeter.send_greetings()

        notified_greetings = greetings_notifier_double.get_spied_notified_greetings()
        expected_greeting_1 = Greeting(
            name="Franco Franchi",
            email="franco@franchi.com",
            birthday=date(1976, 2, 28),
            phone_number="3331112223"
        )
        assert len(notified_greetings) == 1
        assert notified_greetings[0] == expected_greeting_1
