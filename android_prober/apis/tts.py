from typing import Any
from inspect import getmembers, ismethod
from android_prober.wrappers import post
from flask import request
from android_prober.facades import TTS
from android_prober import tts

class TextToSpeech:

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
        return self.tts.say(request.json.get("message"))

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                    value()

def register_tts():
    ttsInterface = TextToSpeech()
    ttsInterface()
    return ttsInterface