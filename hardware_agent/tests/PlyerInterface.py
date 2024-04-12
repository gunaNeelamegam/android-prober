from plyer import __all__

class PlayerInterface:

    def __init__(self) -> None:
        proxy = {
            "module": "plyer",
            "name" : ""
        }
        for feature in __all__:
            exec("from {module} import {name}"
                .format({
                    **proxy,
                    "name": f"{feature}"
                }))

    def register_(self):
        pass

def register_all():
    plyer = PlayerInterface()
    plyer()
    return