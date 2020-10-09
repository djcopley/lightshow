import asyncio

from .animation import run_decorator
from .rainbow import Rainbow


class Rainbowtheater(Rainbow):
    __name__ = "Rainbow Theater"

    def __init__(self, strip, brightness=255, delay=50):
        super().__init__(strip, brightness, delay)

    @run_decorator
    async def run(self):
        while True:
            for j in range(256):
                for q in range(3):
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i + q, self.color_wheel((i + j) % 255))
                    self.strip.show()
                    await asyncio.sleep(self.delay.value / 1000)
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i + q, 0)
