from importlib import import_module


def querry_animations():
    return "rainbow", "rainbowtheater", "colorwipe", "strobe"


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
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = self.__class__.__name__.lower()

    def json(self):
        return self.__dict__


class Slider(Setting):
    def __init__(self, name, value, range, step):
        super().__init__(name, value)
        self.range = range  # Tuple
        self.step = step


class Color(Setting):
    def __init__(self, name, value):
        super().__init__(name, value)
