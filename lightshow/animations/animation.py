"""
Base animation class
"""
# from rpi_ws281x import PixelStrip
from . import *


class Animation:
    """
    Animation base class. All animations should inherit from here.
    """

    __name__ = "Animation"

    def __init__(self, strip, brightness=255):
        """
        Animation constructor method.

        :param strip: LED light strip object
        """
        self.strip = strip
        self._brightness = Slider("brightness", brightness, (0, 255), 1)

        # Variable used to signal stop to the run loop
        self.running = False

    def __str__(self):
        return self.__class__.__name__

    @property
    def brightness(self):
        """
        :return: The brightness
        """
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        """
        Set the brightness value

        :param value: 8bit value (0-255)
        :return: None
        """
        value = int(value)
        self._brightness.value = value & 255
        self.strip.setBrightness(self._brightness.value)

    async def run(self):
        """
        Run the animation. Override this method in all animations. Using coroutines enables processing while animation
        is sleeping.

        Note: run() must catch StopAnimationException() to safely shutdown the animation. Alternatively, use the
        @Animation.check_exit decorator.

        :return: None
        """
        raise NotImplementedError()

    def stop(self):
        """
        Method stops the execution of the animation. Override this method in all animations.

        :return: None
        """
        self.running = False

    def get_settings(self):
        """
        Method returns a list of the animations' settings.

        :return: List of Settings
        """
        settings = [
            self.brightness
        ]
        return settings
