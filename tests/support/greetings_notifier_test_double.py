from birthday_greeter.greetings.greetings_notifier import GreetingsNotifier


class GreetingsNotifierTestDouble(GreetingsNotifier):
    def __init__(self):
        self.notified_greetings = []

    def notify(self, greetings):
        self.notified_greetings.extend(greetings)

    def get_spied_notified_greetings(self):
        return self.notified_greetings[:]
