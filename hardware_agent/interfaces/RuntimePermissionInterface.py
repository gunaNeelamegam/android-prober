from abc import ABC, abstractmethod
from typing import Any
from inspect import getmembers, ismethod
from hardware_agent.utils import RuntimePermission
from hardware_agent.wrappers import get
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

    @run_on_ui_thread
    @get
    def location_permission(self):
        status = self.runtime_perm.location_permission()
        return {"status": status, "permission": "Location Permission Requested"}

    @run_on_ui_thread
    @get
    def bluetooth_permission(self):
        status = self.runtime_perm.blutooth_permission()
        return {"status": status, "permission": "Bluetooth Permission Requested"}

    @run_on_ui_thread
    @get
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
