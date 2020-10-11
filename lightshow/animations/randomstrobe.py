import random
import asyncio

from . import pixel_color
from .strobe import Strobe
from .animation import run_decorator


class Randomstrobe(Strobe):
    __name__ = "Random Strobe"

    def __init__(self, strip, brightness=255, freq=10, duty_cycle=0.5):
        super().__init__(strip, brightness=brightness, freq=freq, duty_cycle=duty_cycle)

    @run_decorator
    async def run(self):
        while True:
            # REFACTOR color_wheel return HTML color maybe? I mean this doesn't bother me that bad...
            # Just think about it for now.
            self._color._value = self.color_wheel(random.randint(0, 255))
            await self._strobe()

    # REFACTOR - remove by name or something in case order changes
    def get_settings(self):
        return super().get_settings()[:-1]  # Remove the last setting (Color)
