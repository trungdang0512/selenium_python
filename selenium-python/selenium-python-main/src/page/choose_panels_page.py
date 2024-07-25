from typing import List

from src.automation.element import Element
from src.enum.panel_enum.panel_type import PanelType
from src.page.base_page import BasePage


class ChoosePanelsPage(BasePage):
    def __init__(self):
        self.panelTableItemsXpath = "//div[contains(text(),'{}')]/following-sibling::table//a"


    def get_panel_table_items(self, panel_name: str) -> List[str]:
        panelTableItems = Element.xpath(self.panelTableItemsXpath)
        panelTableItems.value = panelTableItems.value.format('Chart')
        return [element.text for element in panelTableItems]

