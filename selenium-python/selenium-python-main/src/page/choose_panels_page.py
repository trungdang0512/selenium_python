import time
from typing import List

from src.automation.element import Element
from src.enum.panel_enum.panel_type import PanelType
from src.page.base_page import BasePage


class ChoosePanelsPage(BasePage):
    def __init__(self):
        super().__init__()
        self.panelTableItemsXpath = "//div[contains(text(),'{}')]/following-sibling::table//a"
        self.createNewPanelButton = Element.xpath("//span[contains(@onclick, 'Dashboard.openAddPanel(')]")

    def get_panel_table_items(self, panel_name: PanelType) -> List[str]:
        panelTableItems = Element.xpath(self.panelTableItemsXpath)
        panelTableItems.value = panelTableItems.value.format(panel_name.get_value())
        time.sleep(2)
        return panelTableItems.get_all_texts()

    def click_on_create_new_panel_button(self):
        self.createNewPanelButton.scroll_to()
        time.sleep(1)
        self.createNewPanelButton.click()
