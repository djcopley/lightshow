from flask import render_template
from .app import app, socketio
from .lightshow import lightshow


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def on_connect():
    # On connect emit the current settings
    socketio.emit("power", lightshow.state)
    socketio.emit("settings", lightshow.settings)
    socketio.emit("animations", lightshow.animations)
    socketio.emit("current-animation", lightshow.animation)


@socketio.on('power')
def handle_power():
    lightshow.state = not lightshow.state
    socketio.emit('power', lightshow.state)


# @socketio.on('settings')
# def handle_settings(_settings):
#     socketio.emit('settings', lightshow.settings)
#
#
# @socketio.on('animations')
# def handle_animations(_animations):
#     socketio.emit('current-animation', "rainbow")
