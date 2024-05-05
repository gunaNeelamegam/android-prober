from plyer import gps
from typing import Any
from plyer.facades import GPS as PGPS
from android_prober.facades import GPS
from functools import lru_cache
class GenericGps(GPS):

    """
    FIXME:
        on next release we need's to create the pub sub pattern for sending the message asynchrously
    """
    def __init__(self) -> None:
        self.gps: PGPS = gps
        self.current_location :dict = dict()
        self.gps.configure(on_location = self.on_location_change, on_status= self.on_status_change)
    
    def gps_start(self):
        """
        Start the listener for location change's
        """
        self.gps.start()
        return {
            "status": True,
            "message": "Gps Listener Started Successfully"
        }
    
    def gps_stop(self):
        """
        Stop the Already started Listener which listening for location change's.
        """
        self.gps.stop()
        return {
            "status": True,
            "message": "Gps Listener Stoped Successfully"
        }

    def location(self) -> dict:
        return {
            "status": True,
            "message": f"Current Location {self.gps.current_location}"
        }


    @staticmethod
    def on_status_change(status: Any):
        print("GPS STATUS CHANGES ", status)

    @staticmethod
    def on_location_change(location: dict):
        print("GPS LOCATION : ", location)

@lru_cache
def instance():
    gps_interface =  GenericGps()
    return gps_interface