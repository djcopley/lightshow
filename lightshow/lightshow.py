import threading
import asyncio

from rpi_ws281x import PixelStrip

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
        self._run_thread = None

        # Boolean value (on = True; off = False)
        self._state = False

        # List of animation classes
        self._animations = [get_animation(animation)(strip) for animation in querry_animations()]

        # Default to first animation in the list
        self._animation = 0

        # List of JSON settings
        self._settings = self._animations[self._animation].get_settings()

    @property
    def state(self):
        return self._state

    # REFACTOR
    @state.setter
    def state(self, value):
        self._state = value

        # I spawn a new thread when animations are being started
        if value:
            if not getattr(self._run_thread, "is_alive", lambda: False)():
                pass
                # Create a new animation-thread
                self._run_thread = threading.Thread(name="animation-thread", target=self._run_animation)
                # Start the thread
                self._run_thread.start()
        else:
            if getattr(self._run_thread, "is_alive", lambda: False)():
                # Stop the animation
                self._animations[self._animation].stop()
                # Wait for animation to stop
                self._run_thread.join()
                # Clear the LED strand
                clear_strand(self.strip)

    @property
    def animations(self):
        return list(map(str, self._animations))

    @property
    def animation(self):
        return self._animation

    @animation.setter
    def animation(self, value):
        self._animation = value
        self._settings = self._animations[self._animation].get_settings()
        # REFECTOR
        # Perhamps reset method
        if self.state:
            # This is for restarting the animmation... FUcking aWfuL
            self.state = False
            self.state = True

    @property
    def settings(self):
        return [i.json() for i in self._settings]

    def update_setting(self, index, value):
        """
        Update and individual setting

        :param index: Index updated
        :param value: Value set
        :return: None
        """
        # HACK
        # REFACTOR ASAP
        value = float(value)
        if index == 0:
            self._animations[self._animation].brightness = value
        else:
            self._settings[index].value = value

    def _run_animation(self):
        """
        Private method for starting lightshow animations

        :return:
        """
        # The animations are coroutines
        asyncio.run(self._animations[self._animation].run())


# Start the strip and create a lightstrip object
_strip = PixelStrip(100, 21)
_strip.begin()
lightshow = Lightshow(_strip)  # PixelCount, PinNumber
