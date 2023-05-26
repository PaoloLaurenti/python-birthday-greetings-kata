from datetime import date
from greeter.greetings.greeting import Greeting
from greeter.greetings.sms.sms import Sms
from greeter.greetings.sms.sms_greetings_notifier import SmsGreetingsNotifier
from tests.support.sms_service_test_double import SmsServiceTestDouble


class TestSmsGreetingsNotifier:
    def test_greet_many_friends(self):
        sms_service_spy = SmsServiceTestDouble()
        notifier = SmsGreetingsNotifier(from_phone_number= "3225554447", sms_service=sms_service_spy)
        greetings = [
            Greeting(
                name="Franco Franchi",
                email="franco@franchi.com",
                birthday=date(1974, 4, 22),
                phone_number="3338889991"
            ),
            Greeting(
                name="Luciana Luciani",
                email="luciana@luciani.com",
                birthday=date(1980, 4, 22),
                phone_number="3337776662"
            ),
        ]
        notifier.notify(greetings)

        sms = sms_service_spy.get_sent_sms()
        assert sms == [Sms(from_phone_number= "3225554447", to_phone_number="3338889991", text="Happy birthday Franco Franchi!"),
                       Sms(from_phone_number= "3225554447", to_phone_number="3337776662", text="Happy birthday Luciana Luciani!")]
