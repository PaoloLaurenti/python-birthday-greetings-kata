from pydoc import classname

from greeter.clock import Clock


class FakeImmutableClock(Clock):
    def __init__(self, date):
        self.date = date

    def local_tz_today(self):
        return self.date
