import asyncio

from rpi_ws281x import PixelStrip

from . import pixel_color
from .animation import Animation


class Rainbow(Animation):
    """
    Rainbow Animation class
    """
    def __init__(self, strip, brightness=255, delay=50):
        super().__init__(strip, brightness)
        self.delay = delay

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, value):
        self._delay = value

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
        self.running = True
        while self.running:
            for j in range(256):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.color_wheel((i + j) & 255))
                self.strip.show()
                await asyncio.sleep(self.delay / 1000)

    def get_settings(self):
        settings = [
            {"name": "delay", "type": "slider", "range": (0, 200), "value": self.delay}
        ]
        return super().get_settings() + settings
