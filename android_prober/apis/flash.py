from android_prober.facades import Flash
from android_prober import flash
from android_prober.wrappers import get
from typing import Any
from inspect import getmembers, ismethod
class Flash:
    def __init__(self) -> None:
        self.status = False
        self.flash : Flash = flash

    @get(
        summary = "Flash Off",
        description= "Using this Api Can able to Turn off the flash on android device",
        response_model =  [(201, "Success"), (500, "Failure")]
    )
    def flash_off(self) -> dict:
        message = ""
        if self.status:
            self.flash.off()
            self.flash.release()
            message = "Flash OFF Successfully"
        else:
            message = "Already Flash OFF"

        return {
            "status": True,
            "message":message
        }

    @get(
        summary = "Flash on",
        description= "Using this Api Can able to Turn on the flash on android device",
        response_model =  [(201, "Success"), (500, "Failure")]
    )
    def flash_on(self) -> dict:
        message = ""
        if not self.status:
            self.flash.on()
            message = "Flash ON Successfully"
        else:
            message = "Flash Already On"
        return {
            "status": True,
            "message": message
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()


def register_flash():
    flash_interface = Flash()
    flash_interface()
    return flash_interface