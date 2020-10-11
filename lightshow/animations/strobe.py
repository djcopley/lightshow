import asyncio

from . import *
from .animation import Animation, run_decorator


class Strobe(Animation):
    __name__ = "Strobe"

    def __init__(self, strip, brightness=255, color="#ffffff", freq=10, duty_cycle=0.5):
        """
        Strobe animation

        :param strip: LED light strip object
        :param freq: Frequency of the strobe animation
        :param color: Strand color
        :param duty_cycle: Duty cycle (default = 50%)
        """
        super().__init__(strip, brightness)
        self._freq = Slider("Frequency", freq, (1, 50))
        self._duty_cycle = Slider("Duty cycle", duty_cycle, (0, 1), 0.1, dtype=float)
        self._color = Color("Color", color)

    @property
    def freq(self):
        return self._freq.value

    @freq.setter
    def freq(self, value):
        self._freq.value = value

    @property
    def color(self):
        return self._color.value

    @color.setter
    def color(self, value):
        self._color.value = value

    @property
    def duty_cycle(self):
        return self._duty_cycle.value

    @duty_cycle.setter
    def duty_cycle(self, value):
        self._duty_cycle.value = value

    async def _strobe(self):
        # period = 1 / freq
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()
        await asyncio.sleep((1 / self.freq) * self.duty_cycle)

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, pixel_color(0, 0, 0))
        self.strip.show()
        await asyncio.sleep((1 / self.freq) * (1 - self.duty_cycle))

    @run_decorator
    async def run(self):
        while True:
            await self._strobe()

    def get_settings(self):
        settings = [
            self._freq,
            self._duty_cycle,
            self._color
        ]
        return super().get_settings() + settings
