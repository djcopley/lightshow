import threading
import asyncio

from rpi_ws281x import PixelStrip

from .animations import *
from .animations.rainbow import Rainbow


# TODO Figure out how to get settings back from the website and update the Lightshow class & animations


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
        self._run_thread = threading.Thread(name="animation-thread", target=self._run_animation)

        # Boolean value (on = True; off = False)
        self.state = False

        # List of animation classes
        # self._animations = [Rainbow(strip)]  # Load this from animations backend

        # Animation class of current animation
        self.animation = Rainbow(self.strip)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

        if value:
            if not self._run_thread.is_alive():
                self._run_thread.start()
        else:
            if self._run_thread.is_alive():
                self.animation.stop()
                clear_strand(self.strip)
                self._run_thread.join()

    # @property
    # def animations(self):
    #     # Return string names of animations
    #     return self._animations

    # @property
    # def animation(self):
    #     # Return string name of animation
    #     return self._animation
    #
    # @animation.setter
    # def animation(self, value):
    #     if isinstance(value, str):
    #         # TODO set animation class from string
    #         pass
    #     else:
    #         # Set animation class from string name input
    #         self._animation = value

    def _run_animation(self):
        """
        Private method for starting lightshow animations

        :return:
        """
        asyncio.run(self.animation.run())


# Start the strip and create a lightstrip object
_strip = PixelStrip(100, 21)
_strip.begin()
lightshow = Lightshow(_strip)  # PixelCount, PinNumber
