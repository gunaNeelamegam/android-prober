from android_prober.facades import RuntimePermission
from android.permissions import request_permissions, Permission, check_permission

class AndroidPermission:
    """
        This class provide the wrapper around the runtime permission's in android.
    """
    def __init__(self) -> None:
        self.ble_permissions = [Permission.BLUETOOTH_CONNECT, Permission.BLUETOOTH_SCAN]
        self.location_permissions = [Permission.ACCESS_FINE_LOCATION]

    def check_run_permission(self, permission):
         return check_permission(permission)

    def on_permission_status_change(self, permissions, grants):
        print(f"PERMISSIONS {permissions} GRANTS : {grants}")

    def location_permission(self) -> bool:
        permission_status = {}
        for permission in self.location_permissions:
              response = check_permission(permission)
              permission_status = {**permission_status, permission: response}
              print(f"{permission} : {response}")
        requesting_permissions = filter(lambda permission: not permission_status.get(permission), permission_status)
        request_permissions([*requesting_permissions], self.on_permission_status_change)
        return True

    def blutooth_permission(self) -> bool:
        loc_permission_status = {}
        for permission in self.ble_permissions:
            response = check_permission(permission)
            loc_permission_status = {**loc_permission_status, permission: response}
            print(f"{permission}: {response}")
        requesting_permission = filter(lambda permission: not loc_permission_status.get(permission), loc_permission_status)
        request_permissions([*requesting_permission], self.on_permission_status_change)
        return True

    def telephony_permission(self)-> bool:
        print("REQUESTING TELEPHONY PERMISSION")
        status = check_permission(Permission.READ_PHONE_STATE)
        if not status:
            request_permissions([Permission.READ_PHONE_STATE], self.on_permission_status_change)
            return True
        return True

class AndroidRuntimePermission(RuntimePermission):

    def __init__(self) -> None:
        self.runtime_perm = AndroidPermission()

    
    def location_permission(self):
        status = self.runtime_perm.location_permission()
        return {"status": status, "permission": "Location Permission Requested"}

    def bluetooth_permission(self):
        status = self.runtime_perm.blutooth_permission()
        return {"status": status, "permission": "Bluetooth Permission Requested"}

    def telephony_permission(self):
        status = self.runtime_perm.telephony_permission()
        return {"status": status, "permission": "Telephony Permission Requested"}

def instance():
    run_permission = AndroidRuntimePermission()
    run_permission()
    return run_permission
