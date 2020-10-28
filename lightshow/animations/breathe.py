import asyncio

from . import *
from .animation import Animation, run_decorator


class Breathe(Animation):
    __name__ = "Breathe"

    def __init__(self, strip, brightness=255, color="#ffffff", freq=10):
        """
        Breathe animation

        :param strip: LED light strip object
        :param freq: Frequency of the breathe animation
        :param color: Strand color
        """

        super().__init__(strip, brightness)
        self._speed = Slider("Speed", freq, (1, 50))
        self._color = Color("Color", color)

    @property
    def speed(self):
        return self._speed.value

    @speed.setter
    def speed(self, value):
        self._speed.value = value

    @property
    def color(self):
        return self._color.value

    @color.setter
    def color(self, value):
        self._color.value = value

    def _scale_brightness(self, scale_value, max_steps):
        return self._color * (scale_value / max_steps).value

    async def _breathe(self):
        # 3 bits per binary value, 24 binary values per pixel (RGB), 800 kbps transfer rate
        update_delay = 72 * self.strip.numPixels() / 800000

        minimum_steps = int(1 / update_delay)

        # 4.4 for range of 1 to 5 seconds; 50 for range of speed inputs
        brightness_steps = int(minimum_steps + 4.4 * (50 - self.speed))

        for i in list(range(0, brightness_steps + 1)) + list(reversed(range(0, brightness_steps))):
            for j in range(self.strip.numPixels()):
                self.strip.setPixelColor(j, self._scale_brightness(i, brightness_steps))
            self.strip.show()
            await asyncio.sleep(update_delay)

    @run_decorator
    async def run(self):
        while True:
            await self._breathe()

    def get_settings(self):
        settings = [
            self._speed,
            self._color
        ]
        return super().get_settings() + settings
