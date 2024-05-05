"""
FIMXE:
    Need's to work around all the sensor's in Android
    * List of sensor include's
        * IR Blaster #
"""
from android_prober.facades import Sensor
from plyer.facades import Temperature, Humidity,Barometer,Accelerometer,Gravity,Orientation
from plyer import temperature, humidity, barometer,accelerometer,gravity,orientation
from functools import lru_cache

class GenericSensor(Sensor):

    def __init__(self) -> None:
        self.temperature_sen: Temperature = temperature
        self.humidity_sen: Humidity = humidity
        self.barometer_sen: Barometer = barometer
        self.accelration_sen: Accelerometer = accelerometer
        self.gravity_sen: Gravity = gravity
        self.orientation_sen :Orientation = orientation


    def orientation(self,orientation_type: str = "landscape") -> dict:
        getattr(self.orientation_sen, f"set_{orientation_type}")()
    
   
    def gravity(self) -> dict:
        self.gravity_sen.enable()
        data = {
            "status": True,
            "accelration": self.gravity_sen.gravity
        }
        self.gravity_sen.disable()
        return data
   
    def acceleration(self) -> dict:
        self.accelration_sen.enable()
        data = {
            "status": True,
            "accelration": self.accelration_sen.acceleration
        }
        self.accelration_sen.disable()

        return data

   
    def temperature(self) -> dict:
        self.temperature_sen.enable()
        data = {
            "status": True,
            "temperature": self.temperature_sen.temperature
        }
        self.temperature.disable()
        return data
    
    def humidity(self) -> dict:
        # Supported Android
        self.humidity_sen.enable()
        data = {
            "status": True,
            "humidity": self.humidity_sen.tell
        }
        self.humidity_sen.disable()
        return data
    
    def pressure(self) -> dict:
        self.barometer_sen.enable()
        data = {
            "status": True,
            "pressure": self.barometer_sen.pressure
        }
        self.barometer_sen.disable()
        return data

@lru_cache
def instance():
    sensor_interface = GenericSensor()
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