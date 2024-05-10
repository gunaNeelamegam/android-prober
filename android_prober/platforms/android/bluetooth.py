from jnius import autoclass
from typing import Union, Any
from functools import lru_cache
from android.broadcast import BroadcastReceiver
from android_prober.facades import Bluetooth

System = autoclass("java.lang.System")
class AndroidBluetooth(Bluetooth):
    BluetoothAdapter = autoclass("android.bluetooth.BluetoothAdapter")
    BluetoothDevice  = autoclass("android.bluetooth.BluetoothDevice")
    SERIAL_PORT_PROFILE_UUID = "00001101-0000-1000-8000-00805F9B34FB"

    def __init__(self) -> None:
        self.scanned_devices = set()
        self.connected_device = None
        self.is_connected = False
        self.ble_adapter = self.BluetoothAdapter.getDefaultAdapter()
        self.UUID = autoclass('java.util.UUID')
        self.FOUND = self.BluetoothDevice.ACTION_FOUND
        self.STARTED = self.BluetoothAdapter.ACTION_DISCOVERY_STARTED
        self.FINISHED = self.BluetoothAdapter.ACTION_DISCOVERY_FINISHED
        self.server_socket = None

    def on_scanning(self, context, intent):
        action = intent.getAction()
        if action == self.STARTED:
            self.scanned_devices = None
            self.scanned_devices = set()
            System.out.println("SCANNING STARTED ")

        elif action == self.FOUND:
            device = intent.getParcelableExtra(self.BluetoothDevice.EXTRA_DEVICE);
            name = intent.getExtra(self.BluetoothDevice.EXTRA_NAME)
            if device:
                System.out.println("SCANNING : " + str(name) + str(device.toString()))
                if not name:
                    name = ""
            self.scanned_devices.add(AndroidBluetooth.BleDevice(name, device.toString()))

        elif action == self.FINISHED:
            self.ble_adapter.cancelDiscovery()
            self.boardcast_receiver.stop()
            self.boardcast_receiver = None
            System.out.println("SCANNING STOPED")

    def enable(self) -> bool:
        if (self.ble_adapter and not self.ble_adapter.isEnabled()):
            self.ble_adapter.enable()
        return {
            "status": True,
            "message": "Success Bluetooth Adaptor Disabled"
        }

    def disable(self)-> bool:
        if (self.ble_adapter and self.ble_adapter.isEnabled()):
            self.ble_adapter.disable()
        return {
            "status": True,
            "message": "Success Bluetooth Adaptor Disabled"
        }

    def paired_devices(self):
        if self.ble_adapter:
            bounded_devices = self.ble_adapter.getBondedDevices().toArray()
            response = []
            for device in bounded_devices:
                response.append((device.getName(), device.getAddress()))
        return {
            "success": True,
            "devices": response,
            "message": "Paired Devices"
        }

    def scan(self):
        actions = [self.FOUND, self.STARTED, self.FINISHED]
        self.boardcast_receiver = BroadcastReceiver(self.on_scanning, actions=actions)
        self.boardcast_receiver.start()
        self.ble_adapter.startDiscovery()
        return {
            "success": True,
            "message": "Scanning Started Successfully"
        }

    def is_device_paired(self, remote_info: dict) -> bool:
        name = remote_info.get("name", "").lower()
        mac_address = remote_info.get("mac_address","").lower()
        bounded_devices = self.ble_adapter.getBondedDevices().toArray()

        def is_equal(device):
            if name == device.getName().lower() or mac_address == device.getAddress().lower():
                return True
            return False

        filtered_devices = filter(is_equal, bounded_devices)
        return (True,filtered_devices[0]) if len(filtered_devices) else (False, None)

    def pair(self, mac_address: str):
        message = "Provide Bluetooth Correct Credential's"
        if self.ble_adapter and mac_address.strip() != "":
            device = self.ble_adapter.getRemoteDevice(mac_address)
            if device and device.getBondState() != self.BluetoothDevice.BOND_BONDED:
                device.createBond()
                return {
                    "status": True,
                    "device": (device.getName(), device.getAddress()),
                    "message": "Device Paired Successfully"
                }
            else:
                message = "Device Already in Bonded State"
        
        return {
            "status": False,
            "device": [],
            "message": message
        }

    def connect(self, device_info: dict = {}):
        self.connected_device = None
        device = self.ble_adapter.getRemoteDevice(device_info.get("address"))
        if device and device.getBondState()  != self.BluetoothDevice.BOND_NONE:
            self.connected_device = device.createRfcommSocketToServiceRecord(self.UUID.fromString(self.SERIAL_PORT_PROFILE_UUID))
            self.connected_device.getInputStream()
            self.connected_device.getOutputStream()
            self.connected_device.connect()
            System.out.println("CONNECTED DEVICE : " + str(self.connected_device.isConnected()) + str(self.connected_device.getRemoteDevice().toString()))
        return  {
            "success": True,
            "message": "Device Connection Process Started"
        }
    
    def disconnect(self):
        if self.connected_device:
            System.out.println("DISCONNECTED : " + self.connected_device.isConnected())
            self.connected_device.close()
            self.is_connected = False
            self.connected_device = None
        return {
            "success": True,
            "message": f"Device Disconnected Successfully"
        }
    
    def unpair(self, address: Union[str, Any]):
        if self.ble_adapter and address.strip():
            device = self.ble_adapter.getRemoteDevice(address)
            if (device.getBondState() == self.BluetoothDevice.BOND_BONDED):
                device.removeBond();
        return {
            "success": True,
            "message": f"{address} Unpair Successfully"
        }
    class BleDevice:
        def __init__(self, name ="", address= "") -> None:
            self.name = name
            self.address = address
        
        def __eq__(self, other):
            return isinstance(other, AndroidBluetooth.BleDevice) and (self.name == other.name and self.address == other.address)

        def __hash__(self):
            return hash((self.name, self.address))

@lru_cache
def instance():
    bluetooth_instance = AndroidBluetooth()
    return bluetooth_instance