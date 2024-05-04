from plyer.facades import TTS as PTTS
from android_prober.facades import TTS
from plyer import tts
from functools import lru_cache

class GenericTextToSpeech(TTS):

    def __init__(self) -> None:
        self.tts: PTTS = tts
    
    def say(self, message:str = "Say Hello") -> dict:
        self.tts.speak(message)
        return {
            "message": f"{message} started to speak",
            "status": True
        }
    
@lru_cache
def instance():
    ttsInterface = GenericTextToSpeech()
    return ttsInterface