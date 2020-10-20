"""
The purpose of this app is to test the javascript and HTML on any computer
that supports flask and socketio
"""

from flask import Flask
from flask import render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="../lightshow/templates/", static_folder="../lightshow/static/")
socketio = SocketIO(app)

__version__ = "testing"


class TestLightshow:
    def __init__(self):
        self.state = False
        self.animations = ["Rainbow", "Strobe"]
        self.settings = [{"name": "Brightness", "type": "slider", "range": (0, 255), "step": 1, "value": 255}]
        self.animation = None

    def update_setting(self, index, value):
        print(index, self.settings[index], value)


lightshow = TestLightshow()


@app.route("/")
def home():
    return render_template("home.html", version=__version__)


@app.route("/settings/")
def settings():
    return render_template("settings.html", version=__version__)


@socketio.on("connect")
def on_connect():
    # On connect emit the current settings
    socketio.emit("power", lightshow.state)
    socketio.emit("animations", lightshow.animations)
    socketio.emit("animation", lightshow.animation)
    socketio.emit("settings", lightshow.settings)


@socketio.on("power")
def handle_power():
    lightshow.state = not lightshow.state
    socketio.emit("power", lightshow.state)


@socketio.on("setting")
def handle_settings(index, value):
    lightshow.update_setting(index, value)
    socketio.emit("settings", lightshow.settings)


@socketio.on("animation")
def handle_animations(animation):
    lightshow.animation = animation
    socketio.emit("animation", lightshow.animation)
    socketio.emit("settings", lightshow.settings)


socketio.run(app)
