from abc import ABC, abstractmethod
from hardware_agent.agents import AndroidServiceAgent
from hardware_agent.wrappers import get
from typing import Any
from inspect import getmembers, ismethod

class IAndroidService(ABC):

    @abstractmethod
    def on_headset(self, message):
        pass

    @abstractmethod
    def on_incoming_call(self, message):
        pass

    @abstractmethod
    def on_boot(self, message):
        pass

    @abstractmethod
    def on_reboot(self, message):
        pass


class AndroidService(AndroidServiceAgent):

    @get
    def start_service(self) -> dict:
        response = super().start_service()
        return {
            "message": "Service Started Successfully",
            "status": response
        }

    @get
    def stop_service(self) -> dict:
        status = super().stop_service()
        return {
            "message": "Service Stopped Successfully",
            "status": status
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()


def register_android_service():
    android_service = AndroidService()
    android_service()
    return android_service