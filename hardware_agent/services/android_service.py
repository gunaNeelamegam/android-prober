from time import sleep
from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient
from android.broadcast import BroadcastReceiver
from sys import platform as _sys_platform
from os import environ

def _get_platform():
    kivy_build = environ.get('KIVY_BUILD', '')
    if kivy_build in {'android', 'ios'}:
        return kivy_build
    elif 'P4A_BOOTSTRAP' in environ:
        return 'android'
    elif 'ANDROID_ARGUMENT' in environ:
        return 'android'
    elif _sys_platform in ('win32', 'cygwin'):
        return 'win'
    elif _sys_platform == 'darwin':
        return 'macosx'
    elif _sys_platform.startswith('linux'):
        return 'linux'
    elif _sys_platform.startswith('freebsd'):
        return 'linux'
    return 'unknown'

platform = _get_platform()

if platform == 'android':
    from jnius import autoclass

if platform == 'android':
    PythonService = autoclass('org.kivy.android.PythonService')
    PythonService.mService.setAutoRestartService(True)

CLIENT = OSCClient('localhost', 3002)
stopped = False

def on_broadcast(context, intent):
        extras = intent.getExtras()
        action = intent.getAction()
        if action == Intent.ACTION_HEADSET_PLUG:
            headset_state = bool(extras.get('state'))
            System.out.println("HEADSET STATE : " + str(headset_state))
        else:
            System.out.println("OTHER ACTION", action)


HOST = "0.0.0.0"
PORT = 8250
server = None
System = autoclass("java.lang.System")
Intent = autoclass("android.content.Intent")
broadcast_receiver = BroadcastReceiver(on_broadcast, actions=[Intent.ACTION_HEADSET_PLUG, Intent.ACTION_AIRPLANE_MODE_CHANGED])

def start_server():
    global server
    server = OSCThreadServer()
    server.listen(address = HOST, port = PORT, default = True)

def stop_service():
    global stopped
    broadcast_receiver.stop()
    PythonService.mService.setAutoRestartService(False)
    stopped = False

def register_route():
    server.bind("/stop_service", stop_service)

def get_actions():
    return filter(lambda key: key.startswith("ACTION") , vars(Intent).keys())

def get_categorys():
    return filter(lambda key: key.startswith("CATEGORY"), vars(Intent).keys())

def message_loop():
    broadcast_receiver.start()
    while True:
        sleep(1)
        System.out.println("OPEN SOURCE SERVICE IS RUNNING")
        if stopped:
            break
    server.terminate_server()
    sleep(0.1)
    server.close()
    server = None


if __name__ == '__main__':
    message_loop()
