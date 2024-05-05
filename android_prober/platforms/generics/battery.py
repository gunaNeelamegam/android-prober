from plyer.facades import Battery as PBattery
from android_prober.facades import Battery
from plyer import battery
from functools import lru_cache

class GenericBattery(Battery):

    def __init__(self) -> None:
        self.battery: PBattery = battery
    
    def status(self) -> dict:
        status = self.battery.status
        return {
            "status": True,
             **status
        }
    
@lru_cache
def instance():
    battery_interface =  GenericBattery()
    return battery_interface