from typing import Any
from inspect import getmembers, ismethod
from android_prober.wrappers import get
from android_prober import bluetooth
from android_prober.facades import Bluetooth

class Bluetooth:

    def __init__(self) -> None:
        self.bluetooth: Bluetooth = bluetooth
    @get(
        summary= "Turn on Bluetooth",
        description= "Using this Api we can able to turn on bluetooth\n Platform Support's Android",
        response_model=[(200, 'Success'), (500, 'Error')]
    )
    def enable(self) -> dict:
        return self.bluetooth.enable()

    @get(
        summary= "Turn Off Bluetooth",
        description= "Using this Api we can able to turn off bluetooth\n Platform Support's Android",
        response_model=[(200, 'Success'), (500, 'Error')]
    )
    def disable(self) -> dict:
        return self.bluetooth.disable()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_bluetooth():
    bluetoothAgent = Bluetooth()
    bluetoothAgent()
    return bluetoothAgent
