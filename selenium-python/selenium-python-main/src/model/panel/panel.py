from dataclasses import dataclass

@dataclass
class Panel:
    def __init__(self, display_settings=None, filter=None):
        self.display_settings = display_settings
        self.filter = filter
