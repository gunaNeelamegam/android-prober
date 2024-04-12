from plyer.facades.tts import TTS
from plyer import tts
from abc import ABC, abstractmethod
from typing import Any
from inspect import getmembers, ismethod
from hardware_agent.wrappers import  get,post
from flask import request

class ITTS(ABC):

    @abstractmethod
    def say(self, message: str):
        pass

class TextToSpeechInterface(ITTS):

    def __init__(self) -> None:
        self.tts: TTS = tts

    @post
    def say(self) -> dict:
        message = request.json.get("message", "")
        if not message:
            message = "HELLO WORLD"
        self.tts.speak(message)
        return {
            "message": f"{message} started to speak",
            "status": True
        }

    """
        FIMXE: Need's to compatiable
    """
    # @get(handler_name = "say")
    # def get_say(self):
    #     print("SAY INSIDE GET MEHOD")
    #     return "GET SAY"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                    value()

def register_tts():
    ttsInterface = TextToSpeechInterface()
    ttsInterface()
    return ttsInterface