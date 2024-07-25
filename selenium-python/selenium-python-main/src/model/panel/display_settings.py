from dataclasses import dataclass

from src.enum.panel_enum.panel_type import PanelType
from src.model.data_profile import DataProfile


@dataclass
class DisplaySettings:
    def __init__(self, panel_type=None, data_profile=None, display_name=""):
        self.panel_type = panel_type if panel_type is not None else PanelType.default_panel_type()
        self.data_profile = data_profile
        self.display_name = display_name
