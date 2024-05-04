from android_prober.wrappers import get
from typing import Any
from inspect import getmembers, ismethod
from android_prober.facades import Service
from android_prober import service

class Service:

    def __init__(self) -> None:
        self.service: Service = service 

    @get(
    summary= "Start the BroadCast Receiver as the Service",
    description= "Using this Api We can able to Event's which are broadcasted by the android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def start_service(self) -> dict:
        return self.service.start_service()

    @get(
    summary= "Stop the BroadCast Receiver as the Service",
    description= "Using this Api We can able to Event's which are broadcasted by the android system",
    response_model=[(200, 'Success'), (500, 'Error')]
    )
    def stop_service(self) -> dict:
        return self.stop_service()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for key,value in getmembers(self, predicate= ismethod):
            if not key.startswith('__') and not key.endswith("__"):
                value()


def register_service():
    background_service = Service()
    background_service()
    return background_service