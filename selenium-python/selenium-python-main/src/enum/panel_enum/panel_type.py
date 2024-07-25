import random
from enum import Enum


class PanelType(Enum):
    CHARTS = "Chart"
    INDICATORS = "Indicator"
    REPORTS = "Report"
    HEAT_MAPS = "Heat Map"

    @staticmethod
    def default_panel_type():
        return PanelType.CHARTS

    def get_value(self):
        return self.value
