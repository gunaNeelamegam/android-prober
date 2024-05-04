from plyer import notification
from typing import NamedTuple
from plyer.facades import Notification as PNotification
from android_prober.facades import Notification
from functools import lru_cache

class Message(NamedTuple):
    title: str
    message: str
    toast: bool = True
    timeout : int = 10
    ticker: str = ""

class GenericNotification(Notification):

    def __init__(self) -> None:
        self.notification: PNotification = notification
    
    def notify(self, notification_info: dict) -> dict:
        message = Message(**notification_info)
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


@lru_cache
def instance():
    notificationInterface = GenericNotification()
    return notificationInterface