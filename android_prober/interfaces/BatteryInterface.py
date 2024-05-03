from typing import Any
from inspect import getmembers, ismethod
from plyer.facades.battery import Battery
from plyer import battery

# custom module
from android_prober.wrappers import get
from abc import ABC,abstractmethod

class IBattery(ABC):

    @abstractmethod
    def battery_status(self)->dict:
        pass

class BatteryInterface(IBattery):

    def __init__(self) -> None:
        self.battery: Battery = battery

    @get(
    summary= "Battery Status",
    description= "Using this Api We can able to retrive the battery status in android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def battery_status(self) -> dict:
        status = self.battery.status
        return {
            "status": True,
             **status
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_battery():
    battery_interface =  BatteryInterface()
    battery_interface()
    return battery_interface