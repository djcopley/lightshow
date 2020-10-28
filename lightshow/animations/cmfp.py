"""
Color Magnitude, Frequency Position

This animation displays a color based on the magnitude of the frequency at a position corresponding with frequency.
"""
import asyncio

from scipy.fft import rfft
from . import Slider
from .animation import Animation, run_decorator


class Dynamic(Animation):
    __name__ = "CMFG (Dynamic)"

    def __init__(self, strip, brightness=255):
        super().__init__(strip, brightness)
        self._dithering = Slider("Dithering", 5, (0, 10))
        self._averaging = Slider("Averaging", 5, (0, 10))

    @property
    def dithering(self):
        return self._dithering.value

    @dithering.setter
    def dithering(self, value):
        self._dithering.value = value

    @property
    def averaging(self):
        return self._averaging.value

    @averaging.setter
    def averaging(self, value):
        self._averaging.value = value

    def _dither(self):
        """

        :return: Dithered colors
        """
        pass

    def _average(self):
        """

        :return: FFT Averaging
        """
        pass

    @run_decorator
    async def run(self):
        while True:
            pass
