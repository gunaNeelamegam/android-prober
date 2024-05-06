from typing import Any
from inspect import getmembers, ismethod
from flask import request
from android_prober.facades.email import Email
from android_prober import email
from android_prober.utils.common import Platform
from android_prober.wrappers import get,post
from typing import NamedTuple

class EmailMessage(NamedTuple):
    subject: str
    text: str
    recipient : str
    create_chooser: str


class Email:

    def __init__(self) -> None:
        self.email: Email = email

    @post(
        summary = "Send Email",
        description= "Using this Api Can able to Send Email \n Supported Platform's Android, Linux, Windows, iOS",
        request_model= {
            "recipient" : "string",
            "subject": "string",
            "text": "string",
            "create_chooser": "boolean"
        },
        response_model =  [(201, "Success"), (500, "Failure")]
    )
    def send_mail(self) -> dict:
        """
        {
            "recipient" : "gunag5127@gmail.com",
            "subject": "say hello to all",
            "text": "Hello world from Guna",
            "create_chooser": True
        },
        """
        email_msg = EmailMessage(**request.json)
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

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_email():
    email_interface =  Email()
    email_interface()
    return email_interface