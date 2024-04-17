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
        self.permission = RuntimePermission()
        TesterApp.use_flaskapp()


    def on_pause(self):
        super().on_pause()
        return True

    def telephony_permission(self):
        self.permission.telephony_permission()

    def location_permission(self):
        self.permission.location_permission()

    def bluetooth_permission(self):
        self.permission.blutooth_permission()

    def build(self):
        self.init()
        self.root = Builder.load_string(KV)
        return self.root

if __name__ == '__main__':
    Tester().run()


"""
# Reference for using the MyReceiver which is created as the custom java class inside

from jnius import autoclass
from kivy.logger import Logger
from kivy.clock import  Clock

inside any function which is implicitly called
Clock.schedule_once(self.start, 5)

 def start(self, dt):
        try:
            MyReceiver = autoclass("org.kivy.bootup.MyReceiver")
            Logger.info(f"{str(MyReceiver)=} ON START")
        except Exception as e:
            Logger.info(f" EXCEPTION : {e.args}")

"""