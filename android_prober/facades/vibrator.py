from typing import Any
from inspect import getmembers, ismethod

class Vibrator:
   
    def vibrate(self) -> dict:
        pass

    def cancel_vibrate(self)->dict:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()