from datetime import date
from greeter.greeting import Greeting
from greeter.greetings_notifier import GreetingsNotifier


class Greeter:
    greetings_notifier: GreetingsNotifier

    def __init__(self, friends_gateway, greetings_notifier):
        self.friends_gateway = friends_gateway
        self.greetings_notifier = greetings_notifier

    def send_greetings(self):
        friends = self.friends_gateway.get_friends()
        greetings = map(
            lambda f: Greeting(name=f.name, email=f.email, birthday=f.birthday), friends
        )
        self.greetings_notifier.notify(greetings)
