"""
Base animation class
"""
import asyncio

from . import *


def run_decorator(func):
    async def decorated(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except asyncio.CancelledError:
            return

    return decorated


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
        self._brightness = Slider("brightness", brightness, (0, 255))

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

    @staticmethod
    def color_wheel(pos):
        """
        Generate rainbow colors across 0-255 positions.

        :param int pos: Current position
        """
        if pos < 85:
            return pixel_color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return pixel_color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return pixel_color(0, pos * 3, 255 - pos * 3)

    @run_decorator
    async def run(self):
        """
        Run the animation. Override this method in all animations. Using coroutines enables processing while animation
        is sleeping.

        Note: run() must catch asyncio.CanceledError() to safely shutdown the animation. Alternatively, use the
        @run_decorator decorator.

        :return: None
        """
        raise NotImplementedError()

    def get_settings(self):
        """
        Method returns a list of the animations' settings.

        :return: List of Settings
        """
        settings = [
            self.brightness
        ]
        return settings
