from abc import ABC, abstractmethod
from typing import Any
from android_prober.wrappers import get , post
from inspect import getmembers, ismethod
from flask import request
from android_prober.facades import Audio
from android_prober import audio

class Audio:

    def __init__(self) -> None:
        self.audio: Audio = audio
        self.filepath:str = "/sdcard/test_recorder.3gp"
        self.audio.filepath = self.filepath

    @get(
    summary= "Get the Record State",
    description= "Using this Api We can able to get the state of Recording inside android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def record_state(self):
        return {
            "status": True,
            "state": self.audio.state
        }

    @post(
    summary= "Start Record",
    description= "Using this Api We can able to get the Start of Recording inside android system",
    response_model=[(200, 'Success'), (500, 'Error')],
     request_model = {
            "filepath": "string"
        }
    )
    def start_record(self) -> dict:
        filepath = request.json.get("filepath")
        if filepath:
            self.audio.file_path = filepath
        else:
            self.audio.file_path = self.filepath
        self.audio.start()
        return {
            "status": True,
            "state": self.audio.state,
            "filename": self.filepath
        }

    @get(
    summary= "Stop Record",
    description= "Using this Api We can able to get the Stop of Recording inside android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def stop_record(self) -> dict:
        self.audio.stop()
        return {
            "status": True,
            "state": self.audio.state,
        }

    @post(
        summary= "Play Audio",
        description= "Using this Api We can able to play the audion playback inside android system",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "filepath": "string"
        }
    )
    def play_audio(self) -> dict:
        filepath = request.json.get("filepath")
        if filepath:
            self.audio.file_path = filepath
        else:
            self.audio.file_path = self.filepath

        self.audio.play()
        return {
            "status": True,
            "message": self.audio.state,
            "filename": self.audio.file_path
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_audio():
    audioRecorderInterface = Audio()
    audioRecorderInterface()
    return audioRecorderInterface