"""Need's to follow
    * Install the application inside the release artificat's.
    * We Tried to achive the same functionality as jsonrpc protocol.
    * we need's to invoke the api using the method name.

    example:
        ```python3
        from requests import get,post
        IP_ADDRESS = "0.0.0.0"
        PORT = 5000
        METHOD_NAME = "test"
        get("http://{IP_ADDRESS}:{PORT}/{METHOD_NAME}")
    """

#NOTE: MOBILE AND example may run in same network or else you need's to port forward with the 5000 with your adb command.
#STEPS TO FOLLOW
"""
* use the below command to do.
            <your machine ip> <mobile device ip>
* adb forward tcp:6100 tcp:7100
* After the verify with command.
    * Open the browser with the ip and port http://0.0.0.0:5000/
* please follow through the link [https://medium.com/@godwinjoseph.k/adb-port-forwarding-and-reversing-d2bc71835d43]
"""
from requests import get
from time import sleep
PORT = 5000
HOST = "0.0.0.0"
PROTO = 'http://'


def index():
    response = get(f"{PROTO}{HOST}:{PORT}/")
    try:
        print(response.json())
    except Exception as e:
        print(response.text)

def enable_bluetooth():
    METHOD_NAME = "turn_on_bluetooth"
    response = get(f"{PROTO}{HOST}:{PORT}/{METHOD_NAME}")
    try:
        print(response.json())
    except Exception as e:
        print(response.text)

def disable_bluetooth():
    METHOD_NAME = "turn_off_bluetooth"
    response = get(f"{PROTO}{HOST}:{PORT}/{METHOD_NAME}")
    try:
        print(response.json())
    except Exception as e:
        print(response.text)


if __name__ == "__main__":
    # just for human verification NOT REQUIRED
    index()
    sleep(3) # just for human verification
    enable_bluetooth()
    sleep(3) # just for human verification
    disable_bluetooth()
    sleep(3) # just for human verification