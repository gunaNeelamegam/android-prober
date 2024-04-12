from typing import Any
from inspect import getmembers, ismethod
from flask import Flask

# custom module
from hardware_agent import App
from hardware_agent.wrappers import get,post
from hardware_agent.agents.Bluetooth_Agent import BluetoothAgent

class BluetoothInterface(BluetoothAgent):

    def __init__(self, app: Flask = None) -> None:
        if App.app is None:
            App.app = app

    @get
    def turn_on_bluetooth(self) -> dict:
        status = self.enable_adapter()
        return {
            "status": status,
        }

    @get
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
