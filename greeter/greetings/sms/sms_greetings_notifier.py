from greeter.greetings.sms.sms import Sms


class SmsGreetingsNotifier:
    def __init__(self, from_phone_number, sms_service):
        self._from_phone_number = from_phone_number
        self._sms_service = sms_service

    def notify(self, greetings):
        sms = map(lambda g: self._greeting_to_sms(g), greetings)
        for s in sms:
            self._sms_service.send(s)

    def _greeting_to_sms(self, greeting):
        text = f"Happy birthday {greeting.name}!"
        return Sms(
            from_phone_number=self._from_phone_number,
            to_phone_number=greeting.phone_number,
            text=text,
        )
