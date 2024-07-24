from dataclasses import dataclass, field

from src.enum.panel_enum.chart_type_option import ChartTypeOptions
from src.enum.panel_enum.data_label_checkboxes import DataLabelsCheckBoxes
from src.enum.panel_enum.legends import Legends
from src.enum.panel_enum.series_options import SeriesOptions
from src.enum.panel_enum.style import Styles
from src.model.panel.display_settings import DisplaySettings


@dataclass
class ChartSettings(DisplaySettings):
    super().__init__()
    chart_title: str = ""
    show_title: bool = False
    chart_type: ChartTypeOptions = ChartTypeOptions.PIE
    style: Styles = Styles.default_style()
    category: str = "Select a field..."
    category_caption: str = ""
    series: SeriesOptions = SeriesOptions.DEFAULT
    series_caption: str = ""
    legends: Legends = Legends.default_legend()
    data_label: DataLabelsCheckBoxes = None
