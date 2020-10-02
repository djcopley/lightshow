from .views import *
from .app import socketio


def main():
    socketio.run()


if __name__ == '__main__':
    main()
