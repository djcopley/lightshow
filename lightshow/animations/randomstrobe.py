import random
import asyncio

from . import pixel_color
from .strobe import Strobe
from .animation import run_decorator


class Randomstrobe(Strobe):
    __name__ = "Random Strobe"

    def __init__(self, strip, brightness=255, freq=10, duty_cycle=0.5):
        super().__init__(strip, brightness, None, freq, duty_cycle)

    @run_decorator
    async def run(self):
        while True:
            self.color.value = self.color_wheel(random.randint(0, 255))
            await self._strobe()
