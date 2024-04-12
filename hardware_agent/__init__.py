# Need's to done with better design but it required
from flask import Flask

class App:
    app :Flask = None

    @classmethod
    def set_flaskapp(self, app: Flask):
        App.app  = app

def register_interface(app: Flask):
    if App.app  is None:
        App.app  = app

    from .interfaces.BluetoothInterface import register_all
    register_all()
