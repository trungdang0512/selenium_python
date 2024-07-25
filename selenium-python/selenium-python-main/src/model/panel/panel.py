from dataclasses import dataclass, field
from typing import Union

from src.model.panel.chart_settings import ChartSettings
from src.model.panel.display_settings import DisplaySettings
from src.model.panel.filter import Filters


@dataclass
class Panel:
    displaySettings: Union[DisplaySettings, ChartSettings] = field(default_factory=DisplaySettings)
    filter: Filters = field(default_factory=Filters)

    def __str__(self):
        return f"Panel{{displaySettings={self.displaySettings}, filter={self.filter}}}"
