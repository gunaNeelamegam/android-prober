from plyer.facades.audio import Audio
from plyer import audio
from abc import ABC, abstractmethod
from typing import Any
from hardware_agent.wrappers import get
from inspect import getmembers, ismethod
from hardware_agent.wrappers import post
from flask import request

class IAudio(ABC):

    @abstractmethod
    def stop_record(self) -> dict:
        pass

    @abstractmethod
    def start_record(self) -> dict:
        pass

    @abstractmethod
    def play_audio(self) -> dict:
        pass

    @abstractmethod
    def record_state(self):
        pass

class AudioRecorderInterface(IAudio):

    def __init__(self) -> None:
        self.audio: Audio = audio
        self.filepath:str = "/sdcard/test_recorder.3gp"

    @get
    def record_state(self):
        return {
            "status": True,
            "state": self.audio.state
        }

    @post
    def start_record(self) -> dict:
        self.audio.start()
        return {
            "status": True,
            "state": self.audio.state,
        }

    @post
    def stop_record(self) -> dict:
        self.audio.stop()
        return {
            "status": True,
            "state": self.audio.state,
        }

    @post
    def play_audio(self) -> dict:
        filepath = request.json.get("filepath")
        self.filepath = self.audio.file_path = filepath
        self
        return {
            "status": True,
            "message": self.audio.state
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_audio():
    audioRecorderInterface = AudioRecorderInterface()
    audioRecorderInterface()
    return audioRecorderInterface