from android_prober.proxy_utils import Proxy
from android_prober import facades
from android_prober.app import AndroidProber

bluetooth = Proxy("bluetooth", facades.Bluetooth)
battery = Proxy("battery", facades.Battery)
tts = Proxy("tts", facades.TTS)
sensor = Proxy("sensor", facades.Sensor)
audio = Proxy("audio", facades.Audio)
brightness = Proxy("brightness", facades.Brightness)
call = Proxy("call", facades.Call)
camera = Proxy("camera", facades.Camera)
filechooser = Proxy("filechooser", facades.FileChooser)
email = Proxy("email", facades.Email)
flash = Proxy("flash", facades.Flash)
gps = Proxy("gps", facades.GPS)
notification = Proxy("notification", facades.Notification)
vibrator = Proxy("vibrator", facades.Vibrator)
service = Proxy("service", facades.Service)
runtime_permission = Proxy("runtime_permission", facades.RuntimePermission)