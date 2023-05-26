from greeter.greetings.greetings_notifier import GreetingsNotifier


class GreetingsNotifierAnnouncer(GreetingsNotifier):
    def __init__(self, notifiers):
        self._notifiers = notifiers

    def notify(self, greetings):
        for notifier in self._notifiers:
            notifier.notify(greetings)

