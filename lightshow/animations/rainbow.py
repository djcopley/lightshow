import asyncio

from .animation import Animation, run_decorator
from . import *


class Rainbow(Animation):
    __name__ = "Rainbow"

    def __init__(self, strip, brightness=255, delay=50):
        super().__init__(strip, brightness)
        self.delay = Slider("delay", delay, (10, 200))

    @run_decorator
    async def run(self):
        # Loop until asyncio cancels event
        while True:
            for j in range(256):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.color_wheel((i + j) & 255))
                self.strip.show()
                await asyncio.sleep(self.delay.value / 1000)

    def get_settings(self):
        settings = [
            self.delay
        ]
        return super().get_settings() + settings
