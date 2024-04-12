from plyer.facades.vibrator import Vibrator
from plyer import vibrator
from abc import abstractmethod, ABC
from hardware_agent.wrappers import post, get
from flask import request
from typing import Any
from inspect import getmembers, ismethod

class IVibrate(ABC):

    @abstractmethod
    def vibrate(self) -> dict:
        pass

    @abstractmethod
    def cancel_vibrate(self)->dict:
        pass

class VibrateInterface(IVibrate):

    def __init__(self) -> None:
        self.vibrator : Vibrator = vibrator
        self.support = self.vibrator.exists()

    @get
    def cancel_vibrate(self) -> dict:
        message = ""
        if self.support:
            self.vibrator.cancel()
            message = "Vibration Cancelled"
        else:
            message = "Vibrator is not Supported"
        return {
            "status": True,
            "message": message
        }

    @post
    def vibrate(self) -> dict:
        body = request.json
        vibration_count = body.get("count", 1)
        vibration_pattern = body.get("pattern")
        repeat = body.get("repeat", -1)
        message = ""
        if self.support:
            if vibration_pattern:
                self.vibrator.pattern(pattern = vibration_pattern, repeat = repeat)
            else:
                self.vibrator.vibrate(vibration_count)
            message = "Vibration Started"
        else:
            message = "Vibration Not Supported"

        return {
            "status": True,
            "message": message
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_vibrate():
    vibration_interface = VibrateInterface()
    vibration_interface()
    return vibration_interface