from plyer.facades.tts import TTS
from plyer import tts
from abc import ABC, abstractmethod
from typing import Any
from inspect import getmembers, ismethod
from android_prober.wrappers import  get,post
from flask import request

class ITTS(ABC):

    @abstractmethod
    def say(self, message: str):
        pass

class TextToSpeechInterface(ITTS):

    def __init__(self) -> None:
        self.tts: TTS = tts

    @post(
        summary = "Text to Speech",
        description= "Using this Api Can able to send the text and speechable in android device",
        response_model =  [(201, "Success"), (500, "Failure")],
         request_model = {
            "message": "string"
        }
    )
    def say(self) -> dict:
        message = request.json.get("message", "Say Hello")
        self.tts.speak(message)
        return {
            "message": f"{message} started to speak",
            "status": True
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                    value()

def register_tts():
    ttsInterface = TextToSpeechInterface()
    ttsInterface()
    return ttsInterface