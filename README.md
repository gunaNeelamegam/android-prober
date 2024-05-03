# Library mainly Concentrated on Android and iOS Hardware Testing Library

# Supported platform's android, linux, iOS, windows, mac


## Trying to achive

* `Library to test the android internal Hardware Service's`

> Developed and Tested

* [X]  Bluetooth   ᛒ
    > ABLE TO DO
    * Connect , Disconnect
    * Pair , UnPair
    * Enable, Disable Service Provider
    * look for more..

* [X]  Sensor (Device Supported Sensor's)
* [X] Text To Speech
* [X] Android Runtime Permission's Based on Android API Version
* [X] Media Control's 
* Record Audio ⏺️
* [ ]  Wifi 👎
* [X]  Battery 🔋
* [X] Make Call (or) Dial Intent 📲
* [X] Brightness 🔆
* [X] Gps ➤
* [X] Android Toast 🔔
* [X] Device Sensor Information 📡
* [X] Vibrator 📳
* [X] Share 🔗
* [X] Email 📧
* [X] Camera 📷

> Android Support 📱
* [X] Android Background Service (Broadcast Receiver)

> NOTE  💡
* Using the Android Background Service API you can able to receive the Android Internal Event Message's
    * Aeroplane mode change's 🛩️
    * Headset adaptor state change's 🎧
    * Incoming Phone Call 📲
    * more...

> NOTE 💡 
> 
> `Python Module's`
  * pyjnius
  * plyer
  * flask
  * kivy

##  Build and Run Example's

**Requirements Installation**

```sh
     pip3 install -r requirements
```

**command to genarate apk**

```sh
make build
```

**clean**

```sh
make clean
```

> NOTE 
## Example `main.py`

```python
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
```

> `Way to Use Doc's`

* If you are enabled developer mode. adb daemon will start's or started automatically.

* Run the following command.

```bash
adb forward tcp:5000 tcp:5000
```
* `why tcp:5000` ?
  
  * Inside the Flask Application service will run on tcp:5000 port. So, we trying to expose the port inside the phone 📱 to desktop or development enviroment.

* Open the any web browser 🌐
* [API Documentation](http://localhost:5000/docs) 
* If the previous Link not works try below.
```bash
    http://ipaddress:5000/docs (please replace the ip-address with the mobile connected network ip)
```

### `Looking for` 🚀

* Stablity
* API for All Other Interface's
* FastAPI Intergration
