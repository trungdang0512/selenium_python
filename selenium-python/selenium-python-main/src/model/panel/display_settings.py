from dataclasses import dataclass

from src.enum.panel_enum.panel_type import PanelType
from src.model.data_profile import DataProfile


@dataclass
class DisplaySettings:
    def __init__(self, panel_type=None, data_profile=None, display_name=None):
        self.panelType = PanelType.default_panel_type()
        self.dataProfile = DataProfile
        self.displayName = None
