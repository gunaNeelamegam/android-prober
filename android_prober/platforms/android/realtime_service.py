from time import sleep
from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient
from android.broadcast import BroadcastReceiver
from json import loads
from jnius import autoclass,cast, PythonJavaClass, java_method

PythonActivity = autoclass('org.kivy.android.PythonActivity')
PythonService = autoclass('org.kivy.android.PythonService')

telephony_callback = None
context = PythonService.mService.getApplication().getApplicationContext()
TelephonyManager = autoclass('android.telephony.TelephonyManager')
System = autoclass("java.lang.System")
Intent = autoclass("android.content.Intent")
Context = autoclass("android.content.Context")
Executors = autoclass("java.util.concurrent.Executors")
PythonService.mService.setAutoRestartService(True)
System.out.println("APPLICATION CONTEXT : " + str(context))

class MyCallStateListener(PythonJavaClass):
    __javainterfaces__ = ['android/telephony/TelephonyCallback$CallStateListener']
    __javacontext__ = "app"

    @java_method('(I)V')
    def onCallStateChanged(self, state):
        System.out.println("Call state changed:" + str(state))
        if state == TelephonyManager.CALL_STATE_IDLE:
            System.out.println("Call ended or idle")
        elif state == TelephonyManager.CALL_STATE_RINGING:
            System.out.println("Incoming call ringing from:")
        elif state == TelephonyManager.CALL_STATE_OFFHOOK:
            System.out.println("Outgoing call or call answered")

def unsubscribe_telephonyservice():
    if telephony_callback:
        global telephony_callback
        telephony_manager =  context.getSystemService(Context.TELEPHONY_SERVICE)
        telephony_manager.unregisterTelephonyCallback(telephony_callback)
        telephony_callback = None
           
def subscribe_telephony_service():
    global telephony_callback
    try:
        telephony_manager =  context.getSystemService(Context.TELEPHONY_SERVICE)
        telephony_manager = cast(TelephonyManager, telephony_manager)
        telephony_callback = MyCallStateListener()
        executor = Executors.newSingleThreadExecutor();
        telephony_manager.registerTelephonyCallback(executor , telephony_callback)
    except Exception as e:
        System.out.println("EXCEPTION IN AFTER START" + str(e.args))

HOST = "0.0.0.0"
PORT = 8250
CLIENT_HOST = "192.168.119.122"
CLIENT = OSCClient(CLIENT_HOST, 3002)
server = None
stopped = False
registered = False

def on_boot(extras, intent, context):
    print("BOOT COMPLETED SUCCESSFULLY")

def on_headset(extras, intent, context):
        headset_state = bool(extras.get('state'))
        System.out.println("HEADSET STATE : " + str(headset_state))
        CLIENT.send_message(b"/headset", [headset_state])

def on_incoming_call(extras, intent, context):
    pass

def on_reboot(extras, intent, context):
    CLIENT.send_message(b"/reboot", [b"REBOOT DETECTED"])

def on_call_answer(extras, intent, context):
    CLIENT.send_message(b"/call_answer", [b"INCOMING CALL ACCEPTED"])

def on_airplane_mode(extras, intent, context):
    state = extras.get("state")
    System.out.println("AIRPLANE STATE : " + str(state))
    CLIENT.send_message(b"/airplane_mode",[state])

def on_battery_changed(extras, intent, context):
    System.out.println("ON BATTERY CHANGED")
    BatteryManager = autoclass("android.os.BatteryManager")
    level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
    scale = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1)
    batteryPercentage = ((level // scale) * 100)
    CLIENT.send_message(b"/battery_change", [level, scale, batteryPercentage])

def on_battery_low(extras, intent, context):
    CLIENT.send_message(b"/battery_low", ["BATTERY LOW".encode()])

def on_battery_okay(extras, intent, context):
    CLIENT.send_message(b"/battey_okay", ["BATTERY OKAY".encode()])

def on_call(extras, intent, context):
   try:
    System.out.println("CALL ACTION ")
    phoneNumber = intent.getData();
    if phoneNumber != None:
            number = phoneNumber.getSchemeSpecificPart()
            CLIENT.send_message(b"/call", [str(number).encode()])
   except Exception as e:
       System.out.println("EXCEPTION :" + str(e.args))

def on_screen_on(extras, intent, context):
    CLIENT.send_message(b"/screen_on", [b"SCREEN_ON"])

def on_screen_off(extras, intent, context):
    CLIENT.send_message(b"/screen_off", [b"SCREEN_OFF"])

def on_shutdown(extras, intent, context):
    CLIENT.send_message(b"/shutdown", [b"DEVICE SHUTDOWNING"])

def on_camera_btn(extras, intent, context):
    KeyEvent = autoclass("android.view.KeyEvent")
    keyEvent = intent.getParcelableExtra(Intent.EXTRA_KEY_EVENT);
    System.out.println("KEY EVENT : " + str(keyEvent.getKeyCode()))
    if KeyEvent.KEYCODE_CAMERA:
        CLIENT.send_message(b"/camera_btn", [b"CAMERA BTN CLICKED"])

def on_call_btn(extras, intent, context):
    System.out.println("CALL BTN PRESSED " + str(extras))
    CLIENT.send_message(b"/call_btn", [b"CALL BTN PRESSED"])

def on_answer(extras, intent, context):
    try:
        System.out.println("RINGING CALL")
        telecomManager =  context.getSystemService(Context.TELECOM_SERVICE)
        System.out.println("CALL STATE : " + telecomManager.getCallState())
        if telecomManager:
            telecomManager.acceptRingingCall();
    except Exception as e:
        System.out.println("EXCEPTION : ", str(e.args))

def on_media_btn(extras, intent, context):
    System.out.println("MEDIA BTN PRESSED")
    CLIENT.send_message(b"/media_btn", [b"MEDIA BTN PRESSED"])

def on_search(extras, intent, context):
    SearchManager = autoclass("android.app.SearchManager")
    searched_text = intent.getStringExtra(SearchManager.QUERY)
    System.out.println("SEARCHED WORD" + str(searched_text))
    CLIENT.send_message(b"/search",[str(searched_text).encode()])

def on_outgoing_call(extras, intent, context):
    phone_number = intent.getStringExtra(Intent.EXTRA_PHONE_NUMBER);
    System.out.println("PHONE NUMBER : " + str(phone_number))

ACTIONS = {
    Intent.ACTION_NEW_OUTGOING_CALL: on_outgoing_call,
    Intent.ACTION_HEADSET_PLUG: on_headset,
    Intent.ACTION_AIRPLANE_MODE_CHANGED: on_airplane_mode,
    Intent.ACTION_BOOT_COMPLETED: on_boot,
    Intent.ACTION_LOCKED_BOOT_COMPLETED: on_boot,
    Intent.ACTION_BATTERY_CHANGED:  on_battery_changed,
    Intent.ACTION_REBOOT: on_reboot,
    Intent.ACTION_SCREEN_ON: on_screen_on,
    Intent.ACTION_SCREEN_OFF : on_screen_off,
    Intent.ACTION_SHUTDOWN: on_shutdown,
    Intent.ACTION_CALL_BUTTON: on_call_btn,
    Intent.ACTION_CAMERA_BUTTON: on_camera_btn,
    Intent.ACTION_CALL: on_call,
    Intent.ACTION_ANSWER: on_answer,
    Intent.ACTION_BATTERY_LOW: on_battery_low,
    Intent.ACTION_BATTERY_OKAY: on_battery_okay,
    Intent.ACTION_MEDIA_BUTTON:on_media_btn,
    Intent.ACTION_SEARCH: on_search
}

def on_broadcast(context, intent):
        try:
            extras = intent.getExtras()
            action = intent.getAction()
            if action:
                if callback := ACTIONS.get(action, None):
                    callback(extras, intent, context)
        except Exception as e:
            System.out.println("EXCEPTION :", str(e.args))

intrested_actions = list(ACTIONS.keys())
broadcast_receiver = BroadcastReceiver(on_broadcast, actions = intrested_actions)


def start_server():
    global server
    server = OSCThreadServer()
    server.listen(address = HOST, port = PORT, default = True)

def stop_service():
    global stopped
    broadcast_receiver.stop()
    unsubscribe_telephonyservice()
    PythonService.mService.setAutoRestartService(False)
    stopped = False

def change_client(address: bytes):
    System.out.println("CHANGE CLIENT : " + address.decode())
    address_info: dict = loads(address)
    host:str = address_info.get("host")
    port:int = address_info.get("port")
    global CLIENT
    CLIENT = OSCClient(address = host, port= port)

def register_route():
    server.bind(b"/stop_service", stop_service)
    server.bind(b"/update_address", change_client)

def get_actions():
    return filter(lambda key: key.startswith("ACTION") , vars(Intent).keys())

def get_categorys():
    return filter(lambda key: key.startswith("CATEGORY"), vars(Intent).keys())

def message_loop():
    broadcast_receiver.start()
    while True:
        if stopped:
            break
        sleep(1)
    unsubscribe_telephonyservice()
    server.terminate_server()
    sleep(0.1)
    server.close()
    server = None

if __name__ == '__main__':
    start_server()
    register_route()
    message_loop()
