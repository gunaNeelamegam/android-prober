from flask import request
from typing import Any
from android_prober import sensor
from android_prober.facades import Sensor
from android_prober.wrappers import get, post
from inspect import getmembers, ismethod

class Sensor:

    def __init__(self) -> None:
        self.sensor: Sensor = sensor

    @post(
        summary = "Set the Orientation for the device ",
        description= "Using this Api Can able change the device orientation",
        response_model =  [(201, "Success"), (500, "Failure")],
        request_model = {
           "type": "landscape (or) potrait"
        }
    )
    def orientation(self) -> dict:
        return self.sensor.orientation(request.json.get("type"))
    
    @get(
        summary = "Get the gravity for Device",
        description= "Using this Api Can able to retrive the gravity from gravity sensor",
        response_model =  [(201, "Success"), (500, "Failure")],
    )
    def gravity(self) -> dict:
        return self.sensor.gravity()
    
    @get(
        summary = "Get the Acceleration for Device",
        description= "Using this Api Can able to retrive the acceleration from device sensor",
        response_model =  [(201, "Success"), (500, "Failure")],
    )
    def acceleration(self) -> dict:
        return self.sensor.acceleration()
    
    @get(
        summary = "Get the temperature for Device",
        description= "Using this Api Can able to retrive the temperature from device sensor",
        response_model =  [(201, "Success"), (500, "Failure")],
    )
    def temperature(self) -> dict:
        return self.sensor.temperature()
    
    @get(
        summary = "Get the humidity for Device",
        description= "Using this Api Can able to retrive the humidity from device sensor",
        response_model =  [(201, "Success"), (500, "Failure")],
    )
    def humidity(self) -> dict:
        return self.sensor.humidity()
    
    @get(
        summary = "Get the pressure for Device",
        description= "Using this Api Can able to retrive the pressure from device sensor",
        response_model =  [(201, "Success"), (500, "Failure")],
    )
    def pressure(self) -> dict:
        return self.sensor.pressure()
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_vibrate():
    sensor_interface = Sensor()
    sensor_interface()
    return sensor_interface




"""
 # @get
    # def disable_temperature(self)-> dict:
    #     self.temperature_sen.disable()
    #     return {
    #         "status": True,
    #         "message": "Sensor Disabled Successfully"
    #     }

"""