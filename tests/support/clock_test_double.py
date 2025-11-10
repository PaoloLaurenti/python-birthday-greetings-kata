from birthday_greeter.time.clock import Clock


class ClockTestDouble(Clock):
    def __init__(self):
        self.stubbed_local_tz_today = None

    def stub_local_tz_today(self, date):
        self.stubbed_local_tz_today = date

    def local_tz_today(self):
        return self.stubbed_local_tz_today
