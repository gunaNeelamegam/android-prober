from flask import Flask as _Flask
from datetime import datetime as _datetime
from swagger_gen.swagger import Swagger as _Swagger
from threading import Thread as _Thread
from os import path as _path, curdir as _curdir

# Need's to done with better design but it required
class AndroidProber:
    app : _Flask = None
    swagger: _Swagger = None
    flask_thread = None
    APPNAME = "Prober"
    DOC_ENDPOINT: str = "/docs"
    DOC_TITLE: str = "Android-Prober"

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
        # skipped auto documentation
        cls.start_flask_server(host, port)
        register_interface()
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
        "api": "0.1.0",
        "next_release": str(_datetime.now().date()),
        "status": False
    }


def register_interface():
    """Using this function library try's to use the previously implemented functionality

    Args:
        app (_Flask): _Flask app instance
    """
    # ALL THE INTERFACE WILL RETURN THE INSTANCE OF THE CLASS
    # AUTO MATE 
    from android_prober.apis.bluetooth import register_bluetooth
    from android_prober.apis.call import register_call
    from android_prober.apis.tts import register_tts
    from android_prober.apis.notification import register_notify
    from android_prober.apis.audio import register_audio
    from android_prober.apis.gps import register_gps
    from android_prober.apis.battery import register_battery
    from android_prober.apis.email import register_email
    from android_prober.apis.brightness import register_brightness
    from android_prober.apis.camera import register_camera
    from android_prober.apis.service import register_service
    from android_prober.apis.flash import register_flash



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
    register_flash()
    register_service()