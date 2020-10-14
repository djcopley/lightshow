import asyncio

from . import Slider, set_strand
from .animation import Animation, run_decorator


class Fade(Animation):
    __name__ = "Fade"

    def __init__(self, strip, brightness=255, transition=100):
        super().__init__(strip, brightness)
        self._transition = Slider("Transition", transition, (1, 255))

    @property
    def transition(self):
        return self._transition.value

    @transition.setter
    def transition(self, value):
        self._transition.value = value

    @run_decorator
    async def run(self):
        while True:
            for i in range(256):
                set_strand(self.strip, self.color_wheel(i))
            await asyncio.sleep(self.transition / 1000)

    def get_settings(self):
        settings = [
            self._transition
        ]
        return super().get_settings() + settings
