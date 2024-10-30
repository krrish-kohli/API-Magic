from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib

# Loading environment variables.
load_dotenv()


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.account_sid = os.getenv('account_sid')
        self.auth_token = os.getenv('auth_token')
        self.client = Client(self.account_sid, self.auth_token)

        self.email = os.getenv('MY_EMAIL')
        self.password = os.getenv('PASSWORD')
        self.connection = smtplib.SMTP("smtp.gmail.com")

    def send_message(self, message_body):
        """This function sends the message from virtual number with the message body to the verified number."""

        message = self.client.messages.create(
            body=message_body,
            from_=os.getenv('TWILIO_VIRTUAL_NUMBER'),
            to=os.getenv('TWILIO_VERIFIED_NUMBER'),
        )
        # Prints if message is successfully sent.
        print(message.sid)

    def send_emails(self, users, body):
        """This function sends email with the message body to the user."""
        # Send the letter generated to that person's email address.
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.password)
            for user in users:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=user,
                    msg=f"Subject:Low Price Alert!!\n\n{body}"
                )
