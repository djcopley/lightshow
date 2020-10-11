import asyncio

from .animation import Animation, run_decorator
from . import *


class Rainbow(Animation):
    __name__ = "Rainbow"

    def __init__(self, strip, brightness=255, delay=50):
        super().__init__(strip, brightness)

        # Setup delay slider
        self._delay = Slider("Delay", delay, (10, 200))

    @property
    def delay(self):
        return self._delay.value

    @delay.setter
    def delay(self, value):
        self._delay.value = value

    @run_decorator
    async def run(self):
        # Loop until asyncio cancels event
        while True:
            for j in range(256):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.color_wheel((i + j) & 255))
                self.strip.show()
                await asyncio.sleep(self.delay / 1000)

    def get_settings(self):
        settings = [
            self._delay
        ]
        return super().get_settings() + settings
