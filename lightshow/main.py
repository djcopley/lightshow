from .views import *
from .app import app, socketio


def main():
    socketio.run(app)


if __name__ == '__main__':
    main()
