import random
from enum import Enum
from src.until.get_value_enum import GetValueEnum

class PanelType(Enum, GetValueEnum):
    CHARTS= "Chart"
    INDICATORS= "Indicator"
    REPORTS= "Report"
    HEAT_MAPS= "Heat Map"

    @staticmethod
    def default_panel_type():
        return PanelType.CHARTS

    def get_value(self):
        return self.value