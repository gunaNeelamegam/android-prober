from kivy.app import App
from kivy.lang import Builder
from hardware_agent.utils.permissions import RuntimePermission
from hardware_agent import App as TesterApp

KV = '''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: '30sp'
        Button:
            text: 'telephony_permission'
            on_press: app.telephony_permission()
        Button:
            text: 'bluetoothPermission'
            on_press: app.bluetooth_permission()
        Button:
            text: 'locationPermission'
            on_press: app.location_permission()

    ScrollView:
        Label:
            id: label
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.size[0], None
'''

class Tester(App):

    def init(self):
        # self.flask_thread = None
        self.permission = RuntimePermission()
        TesterApp.use_flaskapp()

        # self.app = Flask(APP_NAME,
        #                 static_folder = self.get_ui_path("static"),
        #                 template_folder = self.get_ui_path("templates"))
        # self.swagger = Swagger(
        #         app= self.app,
        #         title= "test",
        #         url = "/docs"
        # )
        # register_interface(self.app)
        # self.swagger.configure()

    # def get_ui_path(self, folder_name : str):
    #         return path.join(curdir, f"hardware_agent/views/{folder_name}")

    # def start_server(self):
    #     self.app.run(host = HOST, port = PORT, threaded = False, debug = False)

    def telephony_permission(self):
        self.permission.telephony_permission()

    def location_permission(self):
        self.permission.location_permission()

    def bluetooth_permission(self):
        self.permission.blutooth_permission()

    # def start_flask_server(self):
    #     self.flask_thread = Thread(target = self.start_server)
    #     self.flask_thread.daemon = True
    #     self.flask_thread.start()

    def build(self):
        self.init()
        # self.start_flask_server()
        self.root = Builder.load_string(KV)
        return self.root

if __name__ == '__main__':
    Tester().run()
