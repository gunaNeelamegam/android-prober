"""
FIMXE:
    Need's to work around all the sensor's in Android
    * List of sensor include's
        * IR Blaster #
"""

from flask import request
from plyer.facades import Temperature, Humidity,Barometer,Accelerometer,Gravity,Orientation
from plyer import temperature, humidity, barometer,accelerometer,gravity,orientation
from abc import abstractmethod, ABC
from hardware_agent.wrappers import get, post
from typing import Any
from inspect import getmembers, ismethod

class ISensor(ABC):

    @abstractmethod
    def humidity(self) -> dict:
        pass

    @abstractmethod
    def orientation(self) -> dict:
        pass

    @abstractmethod
    def temperature(self)-> dict:
        pass

    @abstractmethod
    def pressure(self)->dict:
        pass

    @abstractmethod
    def acceleration(self)->dict:
        pass

    @abstractmethod
    def gravity(self)->dict:
        pass

class SensorInterface(ISensor):

    def __init__(self) -> None:
        self.temperature_sen: Temperature = temperature
        self.humidity_sen: Humidity = humidity
        self.barometer_sen: Barometer = barometer
        self.accelration_sen: Accelerometer = accelerometer
        self.gravity_sen: Gravity = gravity
        self.orientation_sen :Orientation = orientation

    @post
    def orientation(self) -> dict:
        orientation_type = request.json.get("type", "landscape")
        getattr(self.orientation_sen, f"set_{orientation_type}")()

    @get
    def gravity(self) -> dict:
        self.gravity_sen.enable()
        data = {
            "status": True,
            "accelration": self.gravity_sen.gravity
        }
        self.gravity_sen.disable()
        return data

    @get
    def acceleration(self) -> dict:
        self.accelration_sen.enable()
        data = {
            "status": True,
            "accelration": self.accelration_sen.acceleration
        }
        self.accelration_sen.disable()

        return data

    @get
    def temperature(self) -> dict:
        self.temperature_sen.enable()
        data = {
            "status": True,
            "temperature": self.temperature_sen.temperature
        }
        self.temperature.disable()
        return data

    @get
    def humidity(self) -> dict:
        # Supported Android
        self.humidity_sen.enable()
        data = {
            "status": True,
            "humidity": self.humidity_sen.tell
        }
        self.humidity_sen.disable()
        return data

    @get
    def pressure(self) -> dict:
        self.barometer_sen.enable()
        data = {
            "status": True,
            "pressure": self.barometer_sen.pressure
        }
        self.barometer_sen.disable()
        return data

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()

def register_vibrate():
    sensor_interface = SensorInterface()
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