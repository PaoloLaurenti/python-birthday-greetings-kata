from greeter.greeting import Greeting
from greeter.greetings_notifier import GreetingsNotifier

class GreetingsNotifierSpy(GreetingsNotifier):
    def __init__(self):
        self.notified_greetings = []

    def notify(self, greetings):
        self.notified_greetings.extend(greetings)

    def get_notified_greetings(self):
        return self.notified_greetings[:]
