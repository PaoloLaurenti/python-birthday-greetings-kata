from greeter.greetings.greeting import Greeting
from greeter.greetings.greetings_notifier import GreetingsNotifier


class Greeter:
    greetings_notifier: GreetingsNotifier

    def __init__(self, friends_gateway, clock, greetings_notifier):
        self.friends_gateway = friends_gateway
        self.clock = clock
        self.greetings_notifier = greetings_notifier

    def send_greetings(self):
        local_tz_today = self.clock.local_tz_today()
        friends = self.friends_gateway.get_friends()
        birthday_friends = filter(
            lambda f: self.is_birthday(local_tz_today, f.birthday),
            friends,
        )
        greetings = map(
            lambda f: Greeting(name=f.name, email=f.email, birthday=f.birthday),
            birthday_friends,
        )
        self.greetings_notifier.notify(greetings)

    def is_birthday(self, date, birthday):
        return (
            birthday.day == date.day and birthday.month == date.month
        ) or self.is_29th_feb_birthday_on_28th_feb_of_non_leap_year(date, birthday)

    def is_29th_feb_birthday_on_28th_feb_of_non_leap_year(self, date, birthday):
        return (
            not self.is_leap(date.year)
            and date.day == 28
            and birthday.day == 29
            and date.month == 2
            and birthday.month == 2
        )

    def is_leap(self, year):
        return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)
