class Setting:
    def __init__(self, name):
        self.name = name


class Slider(Setting):
    def __init__(self, name):
        super().__init__(name)


class Color(Setting):
    def __init__(self, name):
        super().__init__(name)


class Animation:
    def __init__(self, strip, brightness=255):
        self.strip = strip
        self.brightness = brightness

    def get_settings(self):
        settings = [
            {"prettyName": "Brightness", "type": "slider", "range": (0, 100), "value": self.brightness}
        ]
        return settings

    def run(self):
        pass
