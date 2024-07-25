from dataclasses import dataclass, field

from src.enum.panel_enum.chart_type_option import ChartTypeOptions
from src.enum.panel_enum.data_label_checkboxes import DataLabelsCheckBoxes
from src.enum.panel_enum.legends import Legends
from src.enum.panel_enum.series_options import SeriesOptions
from src.enum.panel_enum.style import Styles
from src.model.panel.display_settings import DisplaySettings


@dataclass
class ChartSettings(DisplaySettings):
    def __init__(self, panel_type=None, data_profile=None, display_name="",
                 chart_title="", show_title=False, chart_type=ChartTypeOptions.PIE,
                 style=None, category="Select a field...", category_caption="",
                 series=SeriesOptions.DEFAULT, series_caption="",
                 legends=None, data_label=None):
        super().__init__(panel_type, data_profile, display_name)
        self.chart_title = chart_title
        self.show_title = show_title
        self.chart_type = chart_type
        self.style = style if style is not None else Styles.default_style()
        self.category = category
        self.category_caption = category_caption
        self.series = series
        self.series_caption = series_caption
        self.legends = legends if legends is not None else Legends.default_legend()
        self.data_label = data_label
