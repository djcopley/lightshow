import asyncio

from . import Color, pixel_color
from .animation import Animation, run_decorator


class Solid(Animation):
    __name__ = "Solid"

    def __init__(self, strip, brightness=255, color="#0000ff"):
        super().__init__(strip, brightness)
        self._color = Color("Color", color)

    @property
    def color(self):
        return self._color.value

    @color.setter
    def color(self, value):
        self._color.value = value

    @run_decorator
    async def run(self):
        while True:
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.color)
            self.strip.show()
            await asyncio.sleep(0.5)  # Check for cancel

    def get_settings(self):
        settings = [
            self._color
        ]
        return super().get_settings() + settings
