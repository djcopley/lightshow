import os
import elevate

from .views import *
from .app import app, socketio


def main():
    # Elevate to root permissions for GPIO access
    if os.getuid() != 0:
        elevate.elevate()
    socketio.run(app)


if __name__ == '__main__':
    main()
