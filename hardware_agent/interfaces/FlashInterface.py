from plyer.facades.flash import Flash
from plyer import flash
from abc import abstractmethod, ABC
from hardware_agent.wrappers import get
from typing import Any
from inspect import getmembers, ismethod

class IFlash(ABC):

    @abstractmethod
    def flash_on(self)->dict:
        pass

    @abstractmethod
    def flash_off(self) -> dict:
        pass

class FlashInterface(IFlash):
    def __init__(self) -> None:
        self.status = False
        self.flash : Flash = flash

    @get
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

    @get
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
    flash_interface = FlashInterface()
    flash_interface()
    return flash_interface