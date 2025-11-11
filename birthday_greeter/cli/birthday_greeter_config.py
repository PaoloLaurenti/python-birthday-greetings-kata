from dataclasses import dataclass


@dataclass(frozen=True)
class BirthdayGreeterConfig:
    friends_file_path:str
    email_sender: str
    sms_sender: str
