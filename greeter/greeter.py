from datetime import date
from greeter.greeting import Greeting
from greeter.greetings_notifier import GreetingsNotifier


class Greeter:
    greetings_notifier: GreetingsNotifier

    def __init__(self, greetings_notifier):
        self.greetings_notifier = greetings_notifier

    def send_greetings(self):
        greetings = [
            Greeting(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 6, 24),
            )
        ]
        self.greetings_notifier.notify(greetings)
