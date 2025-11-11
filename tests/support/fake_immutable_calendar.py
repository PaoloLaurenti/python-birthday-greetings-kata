from birthday_greeter.time.calendar import Calendar


class FakeImmutableCalendar(Calendar):
    def __init__(self, date):
        self.date = date

    def local_tz_today(self):
        return self.date
