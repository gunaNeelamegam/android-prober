from plyer import audio
from plyer.facades import Audio as PAudio
from android_prober.facades import Audio
from functools import lru_cache

class GenaricAudio(Audio):

    def __init__(self) -> None:
        self.audio: PAudio = audio
        self.filepath:str = "/sdcard/test_recorder.3gp"
        self.audio.filepath = self.filepath

    def record_state(self):
        return {
            "status": True,
            "state": self.audio.state
        }
    
    def start_record(self, filepath: str ) -> dict:
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

    def stop_record(self) -> dict:
        self.audio.stop()
        return {
            "status": True,
            "state": self.audio.state,
        }

    def play_audio(self, filepath) -> dict:
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
    
    # this is required for achiveing the proxy design with rest api intergration
    def load():
        return instance()

@lru_cache
def instance():
    audioRecorderInterface = GenaricAudio()
    return audioRecorderInterface