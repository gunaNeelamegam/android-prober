from functools import lru_cache
from android_prober.facades import Brightness
from plyer.facades.brightness import Brightness as PBrightness
from plyer import brightness

class GenericBrightness(Brightness):

    def __init__(self) -> None:
        self.bright_ness: PBrightness = brightness

    def set_brightness(self, brightness_level: int | str) -> dict:
        if brightness_level:
            self.bright_ness.set_level(brightness_level)
        return {
            "status": True,
            "level": self.bright_ness.current_level(),
        }
    
    def brightness(self)-> dict:
        return {
            "status": True,
            "level": str(self.bright_ness.current_level()),
        }

@lru_cache    
def instance():
    brightness_interface =  GenericBrightness()
    return brightness_interface