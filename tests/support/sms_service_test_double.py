class SmsServiceTestDouble:
    def __init__(self):
        self._sent_sms = []

    def send(self, s):
        self._sent_sms.append(s)

    def get_sent_sms(self):
        return self._sent_sms
