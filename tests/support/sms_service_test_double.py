from birthday_greeter.greetings.sms.sms_service import SmsService


class SmsServiceTestDouble(SmsService):
    def __init__(self):
        self._sent_sms = []

    def send(self, sms):
        self._sent_sms.append(sms)

    def get_spied_sent_sms(self):
        return self._sent_sms
