# Need's to done with better design but it required
from flask import Flask

class App:
    app : Flask = None

    @classmethod
    def set_flaskapp(self, app: Flask):
        App.app  = app

def register_interface(app: Flask):
    if App.app  is None:
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
