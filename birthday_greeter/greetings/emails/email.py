from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    from_address: str
    to_address: str
    subject: str
    text_body: str
