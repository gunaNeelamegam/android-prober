"""
pip or pip3 install android-prober
"""

from kivy.app import AndroidProber
from kivy.lang import Builder
from android_prober import AndroidProber
from android_prober.utils.permissions import RuntimePermission

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

class TestAndroid(AndroidProber):

    def init(self):
        self.permission = RuntimePermission()
        AndroidProber.use_flaskapp()

    def on_pause(self):
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
    TestAndroid().run()