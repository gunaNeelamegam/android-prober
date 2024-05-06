from abc import ABC, abstractmethod
from typing import Any
from inspect import getmembers, ismethod
from android_prober.wrappers import get, post
from flask import request
from android_prober.facades import Call
from android_prober import call

class Call:

    def __init__(self) -> None:
        self.call: Call = call

    @post(
        summary= "Make the Phone Call",
        description= "Using this Api we can able to make call",
        response_model=[(200, 'Success'), (500, 'Error')],
        request_model = {
            "phone_number": "number"
        }
    )
    def make_call(self):
        phone_number = request.json.get("phone_number" , "83973973793")
        return self.call.make_call(tel = phone_number)

    @get(
        summary= "Open the Dial Action",
        description= "Using this Api we can able Open the dialer Activity",
        response_model=[(200, 'Success'), (500, 'Error')],
    )
    def dial_call(self) -> bool:
        self.call.dialcall()
        return {
            "success": True,
            "message": "Dial Activity Opened Successfully"
        }

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_call():
    callInterface = Call()
    callInterface()
    return callInterface