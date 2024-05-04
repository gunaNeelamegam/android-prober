from plyer import camera
from plyer.facades import Camera as PCamera
from android_prober.facades import Camera
from os.path import exists,join
from functools import lru_cache


class GenericCamera(Camera):

    DEFAULT_PATH = ""
    DEFAULT_FILENAME_IMAGE = "test_camera.png"
    DEFAULT_FILENAME_VIDEO = "test_camera.mp4"

    def __init__(self) -> None:
        self.camera: PCamera = camera

    def take_picture(self, filename: str = DEFAULT_FILENAME_IMAGE, path :str = DEFAULT_PATH) -> dict:
        try:
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
    
    def take_video(self, path :str = DEFAULT_PATH, filename: str = DEFAULT_FILENAME_VIDEO ) -> dict:
        try:
            filepath = join(path, filename)
            self.camera.take_video(filename = filepath, on_complete= self.video_callback)
        except Exception as e:
            return {
                "status": False,
                "message": "".join(e.args)
            }

@lru_cache
def instance():
    camera_interface =  GenericCamera()
    return camera_interface