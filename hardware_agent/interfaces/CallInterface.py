from plyer import call
from plyer.facades.call import Call
from abc import ABC, abstractmethod
from typing import Union,Any
from inspect import getmembers, ismethod
from hardware_agent.wrappers import get, post
from flask import request

class ICall(ABC):

    @abstractmethod
    def make_call(self, phone_number: int):
        pass

    @abstractmethod
    def dial_call(self)-> bool:
        pass

class CallInterface(ICall):

    def __init__(self) -> None:
        self.call: Call = call

    @post
    def make_call(self):
        phone_number = request.json.get("number")
        return self.call.makecall(phone_number)

    @get
    def dial_call(self) -> bool:
        return self.call.dialcall()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_call():
    callInterface = CallInterface()
    callInterface()
    return callInterface