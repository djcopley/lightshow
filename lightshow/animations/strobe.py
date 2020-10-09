import asyncio

from . import *
from .animation import Animation, run_decorator


class Strobe(Animation):
    __name__ = "Strobe"

    def __init__(self, strip, brightness=255, freq=10, color=pixel_color(255, 255, 255), duty_cycle=0.5):
        """
        Strobe animation

        :param strip: LED light strip object
        :param freq: Frequency of the strobe animation
        :param color: Strand color
        :param duty_cycle: Duty cycle (default = 50%)
        """
        super().__init__(strip, brightness)
        self.freq = Slider("frequency", freq, (1, 50))
        self.color = Color("color", color)
        self.duty_cycle = Slider("duty cycle", duty_cycle, (0, 1), 0.1)

    @run_decorator
    async def run(self):
        while True:
            # period = 1 / freq
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.color.value)
            self.strip.show()
            await asyncio.sleep((1 / self.freq.value) * self.duty_cycle.value)

            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, pixel_color(0, 0, 0))
            self.strip.show()
            await asyncio.sleep((1 / self.freq.value) * (1 - self.duty_cycle.value))

    def get_settings(self):
        settings = [
            self.freq,
            self.duty_cycle
        ]
        return super().get_settings() + settings
