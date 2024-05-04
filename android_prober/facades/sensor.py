from typing import Any
from inspect import getmembers, ismethod

class Sensor():
    
    def humidity(self) -> dict:
        pass
    
    def orientation(self) -> dict:
        pass
    
    def temperature(self)-> dict:
        pass

    def pressure(self)->dict:
        pass

    def acceleration(self)->dict:
        pass
    
    def gravity(self)->dict:
        pass