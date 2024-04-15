from typing import Any
from inspect import getmembers, ismethod
from flask import request
from plyer.facades.brightness import Brightness
from plyer import brightness

# custom module
from hardware_agent.wrappers import get, post
from abc import ABC,abstractmethod

class IBrightness(ABC):

    @abstractmethod
    def brightness(self)->dict:
        pass

    @abstractmethod
    def set_brightness(self)->dict:
        pass

class BrightnessInterface(IBrightness):

    def __init__(self) -> None:
        self.bright_ness:Brightness = brightness

    @post
    def set_brightness(self) -> dict:
        requested_level:int = request.json.get("level")
        self.bright_ness.set_level(requested_level)
        return {
            "status": True,
            "level": self.bright_ness.current_level,
        }

    @get
    def brightness(self)->dict:
        return {
            "status": True,
            "level": self.bright_ness.current_level,
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_brightness():
    brightness_interface =  BrightnessInterface()
    brightness_interface()
    return brightness_interface