from typing import Any
from inspect import getmembers, ismethod
from flask import Flask, request
from plyer.facades.email import Email
from plyer import email
from platform import platform

# custom module
from hardware_agent.wrappers import get,post
from typing import NamedTuple

class EmailMessage(NamedTuple):
    subject: str
    text: str
    recipient : str
    create_chooser: str


class EmailInterface:

    def __init__(self) -> None:
        self.email: Email = email

    @post
    def send_mail(self) -> dict:
        email_msg = EmailMessage(**request.json)
        if platform()  == "android" and email_msg.create_chooser:
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
    email_interface =  EmailInterface()
    email_interface()
    return email_interface