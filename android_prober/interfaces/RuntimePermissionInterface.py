from abc import ABC, abstractmethod
from typing import Any
from inspect import getmembers, ismethod
from android_prober.utils import RuntimePermission
from android_prober.wrappers import get
from android.runnable import run_on_ui_thread

class IRuntimePermission(ABC):

    @abstractmethod
    def location_permission(self):
        pass

    @abstractmethod
    def bluetooth_permission(self):
        pass

    @abstractmethod
    def telephony_permission(self):
        pass

class RunPermissionInterface(IRuntimePermission):

    def __init__(self) -> None:
        self.runtime_perm = RuntimePermission()

    @get(
        summary = "Request Location Permission",
        description = "Using this API we can request the runtime permission for location in android",
        response_model = [(200, "Success"), (400, "Failure")]
    )
    def location_permission(self):
        status = self.runtime_perm.location_permission()
        return {"status": status, "permission": "Location Permission Requested"}

    @get(
        summary = "Request Bluetooth Permission",
        description = "Using this API we can request the runtime permission for bluetooth in android",
        response_model = [(200, "Success"), (400, "Failure")]
    )
    def bluetooth_permission(self):
        status = self.runtime_perm.blutooth_permission()
        return {"status": status, "permission": "Bluetooth Permission Requested"}

    @get(
        summary = "Request Telephony Permission",
        description = "Using this API we can request the runtime permission for Telephony in android",
        response_model = [(200, "Success"), (400, "Failure")]
    )
    def telephony_permission(self):
        status = self.runtime_perm.telephony_permission()
        return {"status": status, "permission": "Telephony Permission Requested"}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_runpermission():
    run_permission = RunPermissionInterface()
    run_permission()
    return run_permission
