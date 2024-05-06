from typing import Any
from inspect import getmembers, ismethod
from flask import request
from android_prober.facades.brightness import Brightness
from android_prober import brightness
from android_prober.wrappers import get, post
class Brightness:

    def __init__(self) -> None:
        self.bright_ness: Brightness = brightness

    # FIXME: overrides the class dictionary when createing methods with same name
    @post(
        summary= "Set the Device Brightness",
        description= "Using this Api we can able mutate the device brightness",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "level" : "number"
        }
    )
    def set_brightness(self) -> dict:
        requested_level:int = request.json.get("level", 10)
        return self.bright_ness.set_brightness(requested_level)

    @get(
        summary= "Get the Device Brightness",
        description= "Using this Api we can able retrive the device brightness",
        response_model=[(200, 'Success'), (500, 'Error')]
    )
    def brightness(self)->dict:
        return self.bright_ness.brightness()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_brightness():
    brightness_interface =  Brightness()
    brightness_interface()
    return brightness_interface