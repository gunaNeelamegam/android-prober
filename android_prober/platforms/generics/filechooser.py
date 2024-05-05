from plyer import filechooser
from typing import NamedTuple
from plyer.facades import FileChooser as PFileChooser
from android_prober.facades import FileChooser
from functools import lru_cache

class FileChooseRequest(NamedTuple):
    path: str = ""
    multiple : bool = False
    filters: list = []
    preview : bool = False
    title: str = "Tester app"
    show_hidden: bool = False
    icon: str = ""

class GenericFileChooser(FileChooser):

    def __init__(self) -> None:
        self.filechooser: PFileChooser = filechooser


    def open_file(self, file_chooser:dict):
        try:
            data = FileChooseRequest(**file_chooser)
            selected_files = filechooser.open_file(data._asdict())
            return {
                "files": selected_files,
                "status": True,
            }

        except Exception as e:
            return {
                "status": False,
                "message": e.args
            }
    
    def on_result(*args):
        pass

    def save_file(self, file_choosen_info: dict):
        try:
            data = FileChooseRequest(**file_choosen_info)
            response = filechooser.save_file(data._asdict())
            return {
                "status": True,
                "message": "Saved Successfully",
                "files": response
            }
        except Exception as e:
            return {
                "status": False,
                "message": e.args
            }

    def chooser_dir(self, filechoosen_info: dict):
        try:
            data = FileChooseRequest(**filechoosen_info)
            response = filechooser.choose_dir(data._asdict())
            return {
                "status": True,
                "message": "Saved Successfully",
                "files": response
            }
        except Exception as e:
            return {
                "status": False,
                "message": e.args
            }

@lru_cache
def instance():
    filechooser_interface  =  GenericFileChooser()
    return filechooser_interface