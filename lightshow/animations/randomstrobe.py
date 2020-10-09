import random

from . import pixel_color
from .strobe import Strobe
from .animation import run_decorator


class Randomstrobe(Strobe):
    __name__ = "Rainbow Strobe"

    def __init__(self, strip, brightness=255, freq=10, duty_cycle=0.5):
        super().__init__(strip, brightness, None, freq, duty_cycle)

    @run_decorator
    async def run(self):
        self.color.value = pixel_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return await super().run()
