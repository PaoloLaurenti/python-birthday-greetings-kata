import os
from birthday_greeter.greetings.emails.email import Email
from birthday_greeter.greetings.emails.smtp_mailer import SmtpMailer

smtp_config = {
    "smtp_server_address": os.environ["SMTP_SERVER_ADDRESS"],
    "smtp_server_port": os.environ["SMTP_SERVER_PORT"],
    "smtp_server_login": os.environ["SMTP_SERVER_LOGIN"],
    "smtp_server_password": os.environ["SMTP_SERVER_PASSWORD"],
}

mailer = SmtpMailer(smtp_config)
mailer.send(
    Email(
        from_address="sender@test.com",
        to_address="dest@test.com",
        subject="Test subject",
        text_body="Test text body",
    )
)


class SmtpServerConfig:
    smtp_server_address: str
    smtp_server_port: int
    smtp_server_login: str
    smtp_server_password: str
