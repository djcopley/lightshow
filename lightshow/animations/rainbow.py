import asyncio

from .animation import Animation
from . import *


class Rainbow(Animation):
    """
    Rainbow Animation class
    """

    __name__ = "Rainbow"

    def __init__(self, strip, brightness=255, delay=50):
        super().__init__(strip, brightness)
        self.delay = Slider("delay", delay, (10, 200), 1)

    @staticmethod
    def color_wheel(pos):
        """
        Generate rainbow colors across 0-255 positions.

        :param int pos: Current position
        """
        if pos < 85:
            return pixel_color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return pixel_color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return pixel_color(0, pos * 3, 255 - pos * 3)

    async def run(self):
        # REFACTOR
        self.running = True
        while self.running:
            for j in range(256):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.color_wheel((i + j) & 255))

                    # REFACTOR
                    if not self.running:
                        break

                if not self.running:
                    break

                self.strip.show()
                await asyncio.sleep(self.delay.value / 1000)

    def get_settings(self):
        settings = [
            self.delay
        ]
        return super().get_settings() + settings
