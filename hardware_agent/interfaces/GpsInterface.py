from typing import Any
from inspect import getmembers, ismethod
from plyer.facades.gps import GPS
from plyer import gps

# custom module
from hardware_agent.wrappers import get
from abc import ABC,abstractmethod

class IBattery(ABC):

    @abstractmethod
    def location(self)->dict:
        pass

class GpsInterface(IBattery):

    """
    FIXME:
        on next release we need's to create the pub sub pattern for sending the message asynchrously
    """
    def __init__(self) -> None:
        self.gps: GPS = gps
        self.current_location :dict = dict()
        self.gps.configure(on_location = self.on_location_change, on_status= self.on_status_change)

    @get
    def gps_start(self):
        """
        Start the listener for location change's
        """
        self.gps.start()
        return {
            "status": True,
            "message": "Gps Listener Started Successfully"
        }

    @get
    def gps_stop(self):
        """
        Stop the Already started Listener which listening for location change's.
        """
        self.gps.stop()
        return {
            "status": True,
            "message": "Gps Listener Stoped Successfully"
        }

    @get
    def location(self) -> dict:
        return self.current_location

    @staticmethod
    def on_status_change(status: Any):
        print("GPS STATUS CHANGES ", status)

    @staticmethod
    def on_location_change(location: dict):
        print("GPS LOCATION : ", location)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                if "on" not in key:
                    value()

def register_gps():
    gps_interface =  GpsInterface()
    gps_interface()
    return gps_interface