from plyer.facades.notification import Notification
from plyer import notification
from abc import ABC, abstractmethod
from typing import Union,Any,NamedTuple
from inspect import getmembers, ismethod
from hardware_agent.wrappers import post
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

    @post
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