from plyer import call
from plyer.facades.call import Call as PCall
from android_prober.facades import Call
from functools import lru_cache

class GenericCall(Call):

    def __init__(self) -> None:
        self.call: PCall = call

    def make_call(self, phone_number: int | str = "83973973793") -> dict:
        response = self.call.makecall(tel = phone_number)
        print(response, "IN MAKE CALL")
        return {
            "status": True,
            "message": f"Make Call {phone_number}"
        }
    
    def dial_call(self) -> dict:
        self.call.dialcall()
        return {
            "success": True,
            "message": "Dial Activity Opened Successfully"
        }

@lru_cache
def instance():
    callInterface = GenericCall()
    return callInterface