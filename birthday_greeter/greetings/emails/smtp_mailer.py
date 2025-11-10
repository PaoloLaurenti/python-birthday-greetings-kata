import ssl
import smtplib
from email.mime.text import MIMEText
from birthday_greeter.greetings.emails.mailer import Mailer


class SmtpMailer(Mailer):
    def __init__(self, smtp_server_config):
        self.smtp_server_address = smtp_server_config["smtp_server_address"]
        self.smtp_server_port = smtp_server_config["smtp_server_port"]
        self.smtp_server_login = smtp_server_config["smtp_server_login"]
        self.smtp_server_password = smtp_server_config["smtp_server_password"]

    def send(self, email):
        sender = email.from_address
        receiver = email.to_address

        message = MIMEText(email.text_body)
        message["Subject"] = email.subject
        message["From"] = sender
        message["To"] = receiver
        try:
            context = ssl.create_default_context()

            with smtplib.SMTP(
                self.smtp_server_address, self.smtp_server_port
            ) as server:
                server.set_debuglevel(1)
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.smtp_server_login, self.smtp_server_password)
                server.sendmail(sender, receiver, message.as_string())
            print("Sent")
        except Exception as e:
            print("error" + str(e))
