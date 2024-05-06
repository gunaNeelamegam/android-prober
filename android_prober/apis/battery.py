from typing import Any
from inspect import getmembers, ismethod
from android_prober.facades import Battery
from android_prober import battery

from android_prober.wrappers import get

class Battery:

    def __init__(self) -> None:
        self.battery: Battery = battery

    @get(
    summary= "Battery Status",
    description= "Using this Api We can able to retrive the battery status in android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def status(self) -> dict:
        return self.battery.status()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_battery():
    battery_interface =  Battery()
    battery_interface()
    return battery_interface