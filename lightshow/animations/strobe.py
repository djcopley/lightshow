import asyncio

from . import *
from .animation import Animation


class Strobe(Animation):
    def __init__(self, strip, freq=10, color=pixel_color(255, 255, 255), duty_cycle=0.5):
        """
        Strobe animation

        :param strip: LED light strip object
        :param freq: Frequency of the strobe animation
        :param color: Strand color
        :param duty_cycle: Duty cycle (default = 50%)
        """
        super().__init__(strip)
        self.freq = Slider("frequency", freq, (0, 100), 1)
        self.color = Color("color", color)
        self.duty_cycle = Slider("duty cycle", duty_cycle, (0, 1), 0.1)

    async def run(self):
        # period = 1 / freq
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.color.value)
        self.strip.show()
        await asyncio.sleep((1 / self.freq.value) * self.duty_cycle.value)

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
        await asyncio.sleep((1 / self.freq.value) * (1 - self.duty_cycle.value))

    def get_settings(self):
        settings = [
            self.freq,
            self.color,
            self.duty_cycle
        ]
        return super().get_settings() + settings
