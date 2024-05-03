from flask import Flask as _Flask
from _datetime import datetime as _datetime
from swagger_gen.swagger import Swagger as _Swagger
from threading import Thread as _Thread
from os import path as _path, curdir as _curdir

#FIMXE: Use to create with proxy design pattern
# reference https://github.com/kivy/plyer/blob/master/plyer/__init__.py


# Need's to done with better design but it required
class App:

    app : _Flask = None
    swagger: _Swagger = None
    flask_thread = None
    APPNAME = "GUNA_TESTER"
    DOC_ENDPOINT: str = "/docs"
    DOC_TITLE: str = "TESTER"

    @classmethod
    def use_flaskapp(cls, app_name: str = APPNAME , host = "0.0.0.0", port = 5000):
        cls.app = _Flask(app_name,
                        static_folder = cls.get_ui_path("static"),
                        template_folder = cls.get_ui_path("templates"))
        cls.swagger = _Swagger(
                app   = cls.app,
                title = cls.DOC_TITLE,
                url   = cls.DOC_ENDPOINT
        )
        cls.start_flask_server(host, port)
        register_interface(cls.app)
        cls.swagger.configure()
        return cls.app

    @classmethod
    def start_flask_server(cls, host, port):
        cls.flask_thread = _Thread(target = cls.start_server, kwargs= {
             "host": host,
             "port": port
        })
        cls.flask_thread.daemon = True
        cls.flask_thread.start()
        print("FLASK APP STARTED : ", )

    @classmethod
    def get_ui_path(cls, folder_name : str):
            return _path.join(_curdir, f"views/{folder_name}")

    @classmethod
    def start_server(cls, host, port):
        cls.app.run(host = host, port = port, threaded = False, debug = False)

    @staticmethod
    def home_route():
        return {
        "author": "gunaNeelamegam.N",
        "api": 1,
        "next_release": str(_datetime.now().date()),
        "status": False
    }

def register_interface(app: _Flask):
    """Using this function library try's to use the previously implemented functionality

    Args:
        app (_Flask): _Flask app instance
    """
    if App.app is None:
        App.app  = app
    # ALL THE INTERFACE WILL RETURN THE INSTANCE OF THE CLASS

    from .interfaces.BluetoothInterface import register_bluetooth
    from .interfaces.CallInterface import register_call
    from .interfaces.TextToSpeechInterface import register_tts
    from .interfaces.NotificationInterface import register_notify
    from .interfaces.AudioRecorderInterface import register_audio
    from .interfaces.GpsInterface import register_gps
    from .interfaces.BatteryInterface import register_battery
    from .interfaces.EmailInterface import register_email
    from .interfaces.BrightnessInterface import register_brightness
    from .interfaces.CameraInterface import register_camera

    # ANDROID BACKGROUND SERVICE
    from .interfaces.AndroidServiceInterface import register_android_service
    register_android_service()

    # ANDROID RUNTIME PERMISSION INTERFACE
    from .interfaces.RuntimePermissionInterface import register_runpermission
    register_runpermission()

    # REGISTERING THE SERVICE's

    register_camera()
    register_audio()
    register_bluetooth()
    register_tts()
    register_notify()
    register_call()
    register_brightness()
    register_gps()
    register_battery()
    register_email()
