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
        self._delay = Slider("Delay", freq, (1, 50))
        self._color = Color("Color", color)

    @property
    def delay(self):
        return self._delay.value

    @delay.setter
    def delay(self, value):
        self._delay.value = value

    @property
    def color(self):
        return self._color.value

    @color.setter
    def color(self, value):
        self._color.value = value

    async def _breathe(self):
        # 3 bytes per binary packet, 24 binary packets per pixel, 800 kbps transfer rate
        delay_time = self.delay * 72 * self.strip.numPixels() / 800000
        brightness_steps = int(1 / delay_time)

        for i in list(range(0, brightness_steps + 1)) + list(reversed(range(0, brightness_steps))):
            for j in range(self.strip.numPixels()):
                self.strip.setPixelColor(j, (self._color * (i / brightness_steps)).value)
            self.strip.show()
            await asyncio.sleep(delay_time)

    @run_decorator
    async def run(self):
        while True:
            await self._breathe()

    def get_settings(self):
        settings = [
            self._delay,
            self._color
        ]
        return super().get_settings() + settings
