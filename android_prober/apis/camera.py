from typing import Any
from inspect import getmembers, ismethod
from flask import request
from android_prober.facades.camera import Camera
from android_prober import camera
from  os.path import exists,join
from android_prober.wrappers import post

class Camera:

    def __init__(self) -> None:
        self.camera: Camera = camera
        self.DEFAULT_PATH = ""
        self.DEFAULT_FILENAME = "test_camera.png"

    @post(
            summary = "Take Picture",
            description= "Using this Api Can able to Take Picture \n Supported Platform's Android, Linux, Windows, iOS",
            request_model = {
                "filename" : "string"
            },
            response_model= [(201, "Success"), (500, "Failure")]
    )
    def take_picture(self) -> dict:
        try:
            filename = request.json.get("filename", self.DEFAULT_FILENAME)
            path = request.json.get("path", self.DEFAULT_PATH)
            filepath = join(path, filename)
            self.camera.take_picture(filename = filepath, on_complete= self.picture_callback)
            return {
                "filepath":  filepath,
                "status": True,
                "message": "Successfully Picture Captured"
            }
        except Exception as e:
            return {
                "status": False,
                "message": "".join(e.args)
            }

    @staticmethod
    def picture_callback(filepath:str):
        if filepath and exists(filepath):
            #FIMXME: send the indication if the video get completed
            print(f"VIDEO STORED PATH {filepath}")
        else:
            print(f"{filepath} IS NOT EXIST")

    @staticmethod
    def video_callback(filepath:str):
        if filepath and exists(filepath):
            #FIMXME: send the indication if the video get completed
            print(f"VIDEO STORED PATH {filepath}")
        else:
            print(f"{filepath} IS NOT EXIST")

    @post(
        summary = "Capture Video",
        description= "Using this Api Can able to Capture \n Supported Platform's Android, Linux, Windows, iOS",
        request_model= {
            "filename" : "string"
        },
        response_model =  [(201, "Success"), (500, "Failure")]
    )
    def take_video(self, filepath: str) -> dict:
        try:
            filename = request.json.get("filename", self.DEFAULT_FILENAME)
            path = request.json.get("path", self.DEFAULT_PATH)
            filepath = join(path, filename)
            self.camera.take_video(filename = filepath, on_complete= self.video_callback)
        except Exception as e:
            return {
                "status": False,
                "message": "".join(e.args)
            }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                if "callback" not in key:
                    value()

def register_camera():
    camera_interface =  Camera()
    camera_interface()
    return camera_interface