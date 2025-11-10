from dataclasses import dataclass

@dataclass(frozen=True)
class Sms:
    from_phone_number: str
    to_phone_number: str
    text: str
