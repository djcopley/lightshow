import asyncio

from . import Slider, pixel_color
from .animation import Animation, run_decorator

_color_list = (pixel_color(255, 0, 0), pixel_color(0, 255, 255), pixel_color(0, 0, 255))


class Colorwipe(Animation):
    __name__ = "Color Wipe"

    def __init__(self, strip, brightness=255, color_list=_color_list, wipe_delay=20, color_change_delay=10):
        """
        Colorwipe animation

        :param strip: PixelStrip object
        :param brightness: Strip brightness
        :param color_list: List of colors
        :param wipe_delay: time in ms between each pixel update
        :param color_change_delay: time in seconds between each color change
        """
        super().__init__(strip, brightness)
        self.color_list = color_list
        self.wipe_delay = Slider("wipe delay", wipe_delay, (0, 100))
        self.color_change_delay = Slider("color change delay", color_change_delay, (0, 100))

    @run_decorator
    async def run(self):
        while True:
            for color in self.color_list:
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, color)
                    self.strip.show()
                    await asyncio.sleep(self.wipe_delay.value / 1000)
                await asyncio.sleep(self.color_change_delay.value)

    def get_settings(self):
        settings = [
            self.wipe_delay,
            self.color_change_delay
        ]
        return super().get_settings() + settings
