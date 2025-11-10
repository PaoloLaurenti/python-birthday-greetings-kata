import logging
from birthday_greeter.greetings.greetings_notifier import GreetingsNotifier

LOGGER = logging.getLogger(__name__)


class GreetingsNotifierLogger(GreetingsNotifier):
    def __init__(self, greetings_notifier):
        self._greetings_notifier = greetings_notifier

    def notify(self, greetings):
        self._greetings_notifier.notify(greetings)
        for greeting in greetings:
            LOGGER.info("A greeting has been sent to %s", greeting.name)
