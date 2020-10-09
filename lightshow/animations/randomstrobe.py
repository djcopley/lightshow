import random
import asyncio

from . import pixel_color
from .strobe import Strobe
from .animation import run_decorator


class Randomstrobe(Strobe):
    __name__ = "Rainbow Strobe"

    def __init__(self, strip, brightness=255, freq=10, duty_cycle=0.5):
        super().__init__(strip, brightness, None, freq, duty_cycle)

    @run_decorator
    async def run(self):
        while True:
            self.color.value = self.color_wheel(random.randint(0, 255))

            # period = 1 / freq
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.color.value)
            self.strip.show()
            await asyncio.sleep((1 / self.freq.value) * self.duty_cycle.value)

            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, pixel_color(0, 0, 0))
            self.strip.show()
            await asyncio.sleep((1 / self.freq.value) * (1 - self.duty_cycle.value))
