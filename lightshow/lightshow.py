import threading
import time

from .animations import *


class Lightshow:
    """
    This class will contain

    - PixelStrip object
    - ON / OFF Status
    - Iterable of all animations
    - Current animation
    - The thread for running the animations
    """

    def __init__(self, strip):
        # lightstrip object
        self.strip = strip

        # Thread for running animations
        self._run_thread = threading.Thread(name="animation-thread",
                                            target=self.foo)

        # Boolean value (on = True; off = False)
        self.state = False

        # List of animation classes
        self._animations = ["rainbow", "strobe"]  # Load this from animations backend

        # Animation class of current animation
        self._animation = "rainbow"

        self.settings = [{"name": "brightness", "type": "slider", "range": (0, 255), "value": 255}]

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

        # Not sure if I should do this yet
        if value:
            self._start_animation()
        else:
            self._stop_animation()

    @property
    def animations(self):
        # Return string names of animations
        return self._animations

    @property
    def animation(self):
        # Return string name of animation
        return self._animation

    @animation.setter
    def animation(self, value):
        # Set animation class from string name input
        self._animation = value

    def _start_animation(self):
        if not self._run_thread.is_alive():
            self._run_thread.start()

    def foo(self):
        while self.state:
            print("hello world")
            time.sleep(1)

    def _stop_animation(self):
        if self._run_thread.is_alive():
            self._run_thread.join(1)


lightshow = Lightshow(None)
