from plyer import email
from plyer.facades.email import Email as PEmail
from android_prober.utils import Platform
from android_prober.facades import Email
from typing import NamedTuple
from functools import lru_cache

class EmailMessage(NamedTuple):
    subject: str
    text: str
    recipient : str
    create_chooser: str

class EmailInterface(Email):

    def __init__(self) -> None:
        self.email: PEmail = email

    def send_mail(self, email_info: dict) -> dict:
        """
        {
            "recipient" : "gunag5127@gmail.com",
            "subject": "say hello to all",
            "text": "Hello world from Guna",
            "create_chooser": True
        },
        """
        email_msg = EmailMessage(email_info)
        if Platform.is_android()  and email_msg.create_chooser:
            self.email.send(
                recipient = email_msg.recipient,
                subject = email_msg.subject,
                text= email_msg.text,
                create_chooser = email_msg.create_chooser
            )
        else:
            self.email.send(
                recipient = email_msg.recipient,
                subject = email_msg.subject,
                text= email_msg.text
            )
        return {
            "status": True,
            "message": "Email Sended Successfully"
        }

@lru_cache
def instance():
    email_interface =  EmailInterface()
    return email_interface