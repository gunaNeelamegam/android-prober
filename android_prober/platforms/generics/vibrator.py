from plyer import vibrator
from android_prober.facades import Vibrator
from plyer.facades.vibrator import Vibrator as PVibrator
from functools import lru_cache

class GenericVibrator(Vibrator):

    def __init__(self) -> None:
        self.vibrator : PVibrator = vibrator
        self.support = self.vibrator.exists()
    
    def cancel_vibrate(self) -> dict:
        message = ""
        if self.support:
            self.vibrator.cancel()
            message = "Vibration Cancelled"
        else:
            message = "Vibrator is not Supported"
        return {
            "status": True,
            "message": message
        }
    
    def vibrate(self, info: dict) -> dict:
        vibration_count = info.get("count", 1)
        vibration_pattern = info.get("pattern" ,(1,2))
        repeat = info.get("repeat", -1)
        message = ""
        if self.support:
            if vibration_pattern:
                self.vibrator.pattern(pattern = vibration_pattern, repeat = repeat)
            else:
                self.vibrator.vibrate(vibration_count)
            message = "Vibration Started"
        else:
            message = "Vibration Not Supported"

        return {
            "status": True,
            "message": message
        }

@lru_cache
def instance():
    vibration_interface = GenericVibrator()
    return vibration_interface