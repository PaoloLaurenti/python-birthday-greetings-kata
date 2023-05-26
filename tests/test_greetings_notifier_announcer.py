from datetime import date
from greeter.greetings.greeting import Greeting
from greeter.greetings.greetings_notifier_announcer import GreetingsNotifierAnnouncer
from tests.support.greetings_notifier_test_double import GreetingsNotifierTestDouble


class TestGreetingsNotifierAnnouncer:
    def test_notify_all_the_given_notifiers(self):
        greetings_notifier_spy_1 = GreetingsNotifierTestDouble()
        greetings_notifier_spy_2 = GreetingsNotifierTestDouble()
        announcer = GreetingsNotifierAnnouncer([greetings_notifier_spy_1, greetings_notifier_spy_2])

        greetings = [
            Greeting(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
                phone_number="3338889991"
            ),
            Greeting(
                name="Luciana Luciani",
                email="luciana@luciani.com",
                birthday=date(1980, 4, 22),
                phone_number="3337776662"
            ),
        ]
        announcer.notify(greetings)

        greetings_notifier_1 = greetings_notifier_spy_1.get_spied_notified_greetings()
        greetings_notifier_2 = greetings_notifier_spy_2.get_spied_notified_greetings()
        assert greetings_notifier_1 == greetings
        assert greetings_notifier_2 == greetings

