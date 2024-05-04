from plyer.facades import Flash as PFlash
from plyer import flash
from android_prober.facades import Flash
from functools import lru_cache

class GenericFlash(Flash):
    
    def __init__(self) -> None:
        self.status = False
        self.flash : PFlash = flash

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

@lru_cache
def instance():
    flash_interface = GenericFlash()
    return flash_interface