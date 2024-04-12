from flask import render_template, Flask, request
from os import path,curdir
# using the register_interface module all the api's established with
from hardware_agent import register_interface

PORT = 5000
HOST = "0.0.0.0"
APP_NAME = "ZilogicAgent"


def get_ui_path(folder_name : str):
    return path.join(curdir, f"hardware_agent/views/{folder_name}")

app = Flask(APP_NAME,
                        static_folder = get_ui_path("static"),
                        template_folder = get_ui_path("templates"))
register_interface(app)

# class BluetoothInterface(BluetoothAgent):

#     def test(self,*args, **kwargs) -> str:
#         return "Hello world"

# App.set_flaskapp(app)
# agent1 = BluetoothInterface()

@app.get("/")
def index():
    data = {
            "message": f"{APP_NAME} is RUNNING",
            "url": request.url
            }
    return render_template("content.html", **data)


if __name__ == "__main__":
    app.run(host = HOST, port = PORT, threaded = False, debug = False)