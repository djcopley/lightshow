import asyncio

from . import pixel_color
from .animation import Animation, run_decorator


class Solid(Animation):
    __name__ = "Solid"

    def __init__(self, strip, brightness=255, color=pixel_color(255, 0, 0)):
        super().__init__(strip, brightness)
        self.color = color

    @run_decorator
    async def run(self):
        while True:
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.color)
            self.strip.show()
