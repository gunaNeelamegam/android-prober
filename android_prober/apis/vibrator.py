from android_prober.wrappers import post, get
from flask import request
from typing import Any
from inspect import getmembers, ismethod
from android_prober.facades import Vibrator
from android_prober import vibrator

class Vibrator:

    def __init__(self) -> None:
        self.vibrator : Vibrator = vibrator

    @get(
        summary = "Cancel the vibrate",
        description = "Using this API we can request to cancel the on-going vibration android",
        response_model = [(200, "Success"), (400, "Failure")]
    )
    def cancel_vibrate(self) -> dict:
       return self.vibrator.cancel_vibrate()

    @post(
        summary = "Cancel the vibrate",
        description = "Using this API we can request to cancel the on-going vibration android",
        response_model = [(200, "Success"), (400, "Failure")],
        request_model = {
            "count": 1,
            "pattern": [1,2]
        }
    )
    def vibrate(self) -> dict:
        return self.vibrator.vibrate(request.json)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_vibrate():
    vibration_interface = Vibrator()
    vibration_interface()
    return vibration_interface