from greeter.greetings.greetings_notifier import GreetingsNotifier

import logging
LOGGER = logging.getLogger(__name__)

class GreetingsNotifierLogger(GreetingsNotifier):
    def __init__(self, greetings_notifier):
        self._greetings_notifier = greetings_notifier

    def notify(self, greetings):
        self._greetings_notifier.notify(greetings)
        for greeting in greetings:
            LOGGER.info(f'A greeting has been sent to {greeting.name}')
