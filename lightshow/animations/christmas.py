import asyncio

from . import Slider, pixel_color
from .rainbow import Rainbow
from .animation import run_decorator


class Christmas(Rainbow):
    __name__ = "Christmas"

    def __init__(self, strip, brightness=255, delay=500, adjacent_leds=4):
        super().__init__(strip, brightness)

        self._delay = Slider("Delay", delay, (100, 4000), step=100)
        self._adjacent_leds = Slider("Adjacent LEDs", adjacent_leds, (1, 10))

        # Red and green
        self._colors = [pixel_color(255, 255, 255), pixel_color(0, 255, 0)]

    @property
    def adjacent_leds(self):
        return self._adjacent_leds.value

    @adjacent_leds.setter
    def adjacent_leds(self, num_leds):
        self._adjacent_leds.value = num_leds

    @run_decorator
    async def run(self):
        while True:
            for color_idx, color in enumerate(self._colors):
                for pixel_offset in range(color_idx, self.strip.numPixels(), self.adjacent_leds):
                    for contiguous_color in range(self.adjacent_leds):
                        self.strip.setPixelColor(pixel_offset + contiguous_color, color)
            self._colors = self._colors[::-1]
            self.strip.show()
            await asyncio.sleep(self.delay / 1000)

    def get_settings(self):
        settings = [
            self._adjacent_leds
        ]
        return super().get_settings() + settings
