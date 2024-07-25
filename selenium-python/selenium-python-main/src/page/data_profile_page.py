import time

from src.automation.element import Element
from src.enum.data_profiles_enum.item_type import ItemType
from src.enum.data_profiles_enum.related_data import RelatedData
from src.model.data_profile import DataProfile
from src.page.base_page import BasePage


class DataProfilePage(BasePage):
    def __init__(self):
        super().__init__()
        self.addNewLink = Element.xpath("//a[@href='profile.jsp?action=create' and text()='Add New']")
        self.nameTextBox = Element.xpath("//input[@id='txtProfileName']")
        self.itemTypeSelection = Element.xpath("//select[@id='cbbEntityType']")
        self.relatedDataSelection = Element.xpath("//select[@id='cbbSubReport']")
        self.finishButton = Element.xpath("//input[@value='Finish']")

    def click_on_add_new_link(self):
        time.sleep(1)
        self.addNewLink.click()

    def enter_name_text_box(self, name: str):
        if name is not None:
            self.nameTextBox.enter(name)

    def select_item_type(self, type: ItemType):
        if type is not None:
            self.itemTypeSelection.select_by_text(type.get_value())

    def select_related_data(self, related_data: RelatedData):
        if related_data is not None:
            self.relatedDataSelection.select_by_text(related_data.get_value())

    def click_on_finish_button(self):
        self.finishButton.click()

    def fill_new_data_profile_info(self, data_profile: DataProfile):
        self.enter_name_text_box(data_profile.dataProfileName)
        self.select_item_type(data_profile.itemType)
        self.select_related_data(data_profile.relatedData)

    def create_new_data_profile(self, data_profile: DataProfile):
        time.sleep(2)
        self.fill_new_data_profile_info(data_profile)
        self.click_on_finish_button()

