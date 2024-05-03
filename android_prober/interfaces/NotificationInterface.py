from plyer.facades.notification import Notification
from plyer import notification
from abc import ABC, abstractmethod
from typing import Union,Any,NamedTuple
from inspect import getmembers, ismethod
from android_prober.wrappers import post
from flask import request


class Message(NamedTuple):
    title: str
    message: str
    toast: bool = True
    timeout : int = 10
    ticker: str = ""


class INotification(ABC):

    @abstractmethod
    def notify(self) -> dict:
        pass

class NotificationInterface(INotification):

    def __init__(self) -> None:
        self.notification: Notification = notification

    @post(
        summary = "Start the GPS",
        description= "Using this Api Can able to start the gps listener if the location change's response is given through socket's",
        response_model =  [(201, "Success"), (500, "Failure")],
        request_model = {
            "title": "string",
            "message": "string",
            "toast": "boolean",
            "timeout": "number",
        }
    )
    def notify(self) -> dict:
        json = request.json
        message = Message(**json)
        self.notification.notify(
            title = message.title,
            message = message.message,
            toast = message.toast,
            timeout = message.timeout,
            ticker = message.ticker
        )
        return {
            "status":True,
            "message": "Notification Sended Successfully"
        }


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_notify():
    notificationInterface = NotificationInterface()
    notificationInterface()
    return notificationInterface