from flask import Flask
from os import path,curdir
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from threading import Thread

from hardware_agent.agents import AndroidServiceAgent
from hardware_agent import register_interface

if platform == 'android':
    from jnius import autoclass
    from android import mActivity


KV = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '30sp'
        Button:
            text: 'start services'
            on_release: app.start_service()
        Button:
            text: 'stop services'
            on_release: app.stop_service()

    ScrollView:
        Label:
            id: label
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.size[0], None

'''

SERVICE_PORT = 8251
CLIENT_PORT = 8250
PORT = 6000
HOST = "0.0.0.0"
APP_NAME = "TesterAgent"


class Tester(App):

    def init(self):
        # this is one way for start and stop the service
        self.service = AndroidServiceAgent()
        self.flask_thread = None
        self.app = Flask(APP_NAME,
                        static_folder = self.get_ui_path("static"),
                        template_folder = self.get_ui_path("templates"))
        self.register_route()
        register_interface(self.app)

    def get_ui_path(self, folder_name : str):
            return path.join(curdir, f"hardware_agent/views/{folder_name}")

    def start_server(self):
        self.app.run(host = HOST, port = PORT, threaded = False, debug = False)

    def start_flask_server(self):
        self.flask_thread = Thread(target = self.start_server)
        self.flask_thread.daemon = True
        self.flask_thread.start()

    def build(self):
        self.init()
        self.start_flask_server()
        self.root = Builder.load_string(KV)
        return self.root

    @staticmethod
    def index():
        return "Hello world"

    def register_route(self):
        self.app.add_url_rule("/", self.index)

    def stop_service(self) -> bool:
        if platform == "android":
            self.service.service.stop(mActivity)

    def start_service(self):
        if platform == 'android':
            self.service.service.start(mActivity,'')

if __name__ == '__main__':
    Tester().run()
