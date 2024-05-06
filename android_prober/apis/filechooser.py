from typing import Any
from inspect import getmembers, ismethod
from flask import request
from android_prober import filechooser
from android_prober.facades import FileChooser

# custom module
from android_prober.wrappers import post

mime_type = {
        "doc": "application/msword",
        "docx": "application/vnd.openxmlformats-officedocument." +
                "wordprocessingml.document",
        "ppt": "application/vnd.ms-powerpoint",
        "pptx": "application/vnd.openxmlformats-officedocument." +
                "presentationml.presentation",
        "xls": "application/vnd.ms-excel",
        "xlsx": "application/vnd.openxmlformats-officedocument." +
                "spreadsheetml.sheet",
        "text": "text/*",
        "pdf": "application/pdf",
        "zip": "application/zip",
        "image": "image/*",
        "video": "video/*",
        "audio": "audio/*",
        "application": "application/*"}

from typing import NamedTuple

class FileChooseRequest(NamedTuple):
    path: str = ""
    multiple : bool = False
    filters: list = []
    preview : bool = False
    title: str = "Tester app"
    show_hidden: bool = False
    icon: str = ""

class FileChooser:

    def __init__(self) -> None:
        self.filechooser:FileChooser = filechooser

    @post(
        summary= "Open the file chooser window",
        description= "Using this Api we can able open and select the files",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "path": "string",
            "filters": "list",
            "preview": "boolean",
            "show_hidden": "boolean",
            "title": "string",
            "multiple": 'boolean'
        }
    )
    def open_file(self):
        try:
            data = FileChooseRequest(**request.json)
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

    @post(
        summary= "Open the file chooser window",
        description= "Using this Api we can able save the file",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "path": "string",
            "filters": "list",
            "preview": "boolean",
            "show_hidden": "boolean",
            "title": "string",
            "multiple": 'boolean'
        }
    )
    def save_file(self):
        try:
            data = FileChooseRequest(**request.json)
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

    @post(
        summary= "Open the file chooser window in specific directory",
        description= "Using this Api we can able open and select the files",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "path": "string",
            "filters": "list",
            "preview": "boolean",
            "show_hidden": "boolean",
            "title": "string",
            "multiple": 'boolean'
        }
    )
    def chooser_dir(self):
        try:
            data = FileChooseRequest(**request.json)
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


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_filechooser():
    filechooser_interface  =  FileChooser()
    filechooser_interface()
    return filechooser_interface