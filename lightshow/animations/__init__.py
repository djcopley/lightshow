from rpi_ws281x import PixelStrip


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
