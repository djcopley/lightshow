from flask import render_template

from . import __version__
from .app import app, socketio
from .lightshow import lightshow


@app.route("/")
def index():
    return render_template("index.html", version=__version__)


@socketio.on("connect")
def on_connect():
    # On connect emit the current settings
    socketio.emit("power", lightshow.state)
    socketio.emit("animations", lightshow.animations)
    socketio.emit("animation", lightshow.animation)
    socketio.emit("settings", lightshow.settings)


@socketio.on('power')
def handle_power():
    lightshow.state = not lightshow.state
    socketio.emit('power', lightshow.state)


@socketio.on('setting')
def handle_settings(index, value):
    lightshow.update_setting(index, value)
    socketio.emit('settings', lightshow.settings)


@socketio.on('animation')
def handle_animations(animation):
    lightshow.animation = animation
    socketio.emit('animation', lightshow.animation)
    socketio.emit('settings', lightshow.settings)
