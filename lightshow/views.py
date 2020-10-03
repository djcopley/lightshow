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
    socketio.emit("animations", list(map(str, lightshow.animations)))
    socketio.emit("settings", lightshow.animation.get_settings())
    socketio.emit("current-animation", str(lightshow.animations[0]))


@socketio.on('power')
def handle_power():
    lightshow.state = not lightshow.state
    socketio.emit('power', lightshow.state)


@socketio.on('settings')
def handle_settings(_settings):
    print(_settings)
    # socketio.emit('settings', lightshow.settings)


@socketio.on('animations')
def handle_animations(_animations):
    print(_animations)
    # socketio.emit('current-animation', "rainbow")
