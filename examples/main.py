from kivy.app import App
from kivy.lang import Builder
from android_prober import AndroidProber, bluetooth, brightness, battery, tts, runtime_permission

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
        self.permission = runtime_permission
        AndroidProber.use_flaskapp()
        
    def on_pause(self):
        super().on_pause()
        return True

    def telephony_permission(self):
        self.permission.telephony_permission()
    
    def location_permission(self):
        self.permission.location_permission()
       
    def bluetooth_permission(self):
        self.permission.bluetooth_permission()

    def example(self):
         # tts.say("Helo world")        
        # print(brightness)
        # print(brightness.brightness())
        # tts.say("HELLO WORLD")
        # battery.battery_status()
        # self.permission.location_permission()
        pass
    
    def build(self):
        self.init()
        self.root = Builder.load_string(KV)
        return self.root

if __name__ == '__main__':
    Tester().run()
