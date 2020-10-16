from importlib import import_module


def querry_animations():
    return "rainbow", "rainbowtheater", "solid", "colorwipe", "strobe", "randomstrobe", "fade", "breathe"


def get_animation(name: str):
    return getattr(import_module("{}.{}".format(__name__, name)), name.capitalize())


def pixel_color(r, g, b, w=0):
    """
    Color for our LED strand. For some reason our ws chips are RBG ordered.

    :param r: red
    :param g: green
    :param b: blue
    :param w: white
    :return: int of color data
    """
    return ((w & 255) << 24) | ((r & 255) << 16) | ((b & 255) << 8) | (g & 255)


def clear_strand(strip):
    set_strand(strip, pixel_color(0, 0, 0))


def set_strand(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


class Setting:
    def __init__(self, name, value, dtype=int, callback=None):
        self.name = name
        self.dtype = dtype
        self.callback = callback
        self.value = value
        self.type = self.__class__.__name__.lower()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.dtype(value)
        if self.callback:
            self.callback(self._value)

    def json(self):
        return {"name": self.name, "value": self.value, "type": self.type}


class Slider(Setting):
    def __init__(self, name, value, range, step=1, dtype=int, callback=None):
        super().__init__(name, value, dtype, callback)
        self.range = range  # Tuple of two values
        self.step = step  # Step size on the slider

    def json(self):
        settings = [
            self.range,
            self.step
        ]
        return {"name": self.name, "value": self.value, "type": self.type, "range": self.range, "step": self.step}


class Color(Setting):
    def __init__(self, name, value, dtype=str, callback=None):
        super().__init__(name, value, dtype, callback)
        self.html_color = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        """
        Convert HTML color value to pixel_color

        :param value: HTML color value in format '#ffffff'
        :return: None
        """
        self.html_color = value
        self._value = pixel_color(int(value[1:3], 16), int(value[3:5], 16), int(value[5:7], 16))
        if self.callback:
            self.callback(self._value)

    def json(self):
        return {"name": self.name, "value": self.html_color, "type": self.type}
