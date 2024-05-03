from flask import render_template, Flask,request
from android_prober import AndroidProber

PORT = 6000
HOST = "0.0.0.0"

app = Flask(__name__, static_folder="static", template_folder="templates")
AndroidProber.use_flaskapp() # application trigger's the app


@app.get("/")
def index():
    return render_template("content.html",
                            data = {"message": "ble agent runing",
                                     "url": request.url})

if __name__ == "__main__":
    app.run(host = HOST, port = PORT,debug = False, threaded=False)
