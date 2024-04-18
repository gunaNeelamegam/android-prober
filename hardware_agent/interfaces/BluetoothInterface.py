from typing import Any
from inspect import getmembers, ismethod
from flask import Flask

from hardware_agent import App
from hardware_agent.wrappers import get
from hardware_agent.agents import BluetoothAgent

class BluetoothInterface(BluetoothAgent):

    def __init__(self, app: Flask = None) -> None:
        super().__init__()
        if App.app is None:
            App.app = app

    @get(
        summary= "Turn on Bluetooth",
        description= "Using this Api we can able to turn on bluetooth\n Platform Support's Android",
        response_model=[(200, 'Success'), (500, 'Error')]
    )
    def turn_on_bluetooth(self) -> dict:
        status = self.enable_adapter()
        return {
            "status": status,
        }

    @get(
        summary= "Turn Off Bluetooth",
        description= "Using this Api we can able to turn off bluetooth\n Platform Support's Android",
        response_model=[(200, 'Success'), (500, 'Error')]
    )
    def turn_off_bluetooth(self) -> dict:
        status = self.disable_adapter()
        return {
            "status": status,
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if key not in dir(BluetoothAgent) :
                if not key.startswith('__') and not key.endswith("__"):
                    value()

def register_bluetooth():
    bluetoothAgent = BluetoothInterface()
    bluetoothAgent()
    return bluetoothAgent
