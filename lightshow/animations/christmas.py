import asyncio

from . import Slider, pixel_color
from .rainbow import Rainbow
from .animation import run_decorator


class Christmas(Rainbow):
    __name__ = "Christmas"

    def __init__(self, strip, brightness=255, delay=500):
        super().__init__(strip, brightness)

        self._delay = Slider("Delay", delay, (200, 2000))

        # Red and green
        self._colors = [pixel_color(255, 0, 0), pixel_color(0, 255, 0)]

    @run_decorator
    async def run(self):
        while True:
            for color_idx, color in enumerate(self._colors):
                for pixel_offset in range(0, self.strip.numPixels(), len(self._colors)):
                    self.strip.setPixelColor(color_idx + pixel_offset, color)
            self._colors = self._colors[::-1]
            self.strip.show()
            await asyncio.sleep(self.delay / 1000)
