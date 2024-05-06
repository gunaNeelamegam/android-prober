from android_prober import notification
from android_prober.facades import Notification
from inspect import getmembers, ismethod
from android_prober.wrappers import post
from flask import request
from typing import Any

class Notification:

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
        return self.notification.notify(request.json)


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_notify():
    notificationInterface = Notification()
    notificationInterface()
    return notificationInterface