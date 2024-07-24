import time

import allure

from src.automation.element import Element
from src.model.page import Page
from src.page.base_page import BasePage


class CreateNewPageDialog(BasePage):
    def __init__(self):
        self.pageNameTextBox = Element.xpath("//input[@id='name']")
        self.parentPageSelection = Element.xpath("//select[@id='parent']")
        self.numberOfColumnSelection = Element.xpath("//select[@id='columnnumber']")
        self.displayAfterSelection = Element.xpath("//select[@id='afterpage']")
        self.publicCheckbox = Element.xpath("//input[@id='ispublic']")
        self.okButton = Element.xpath("//input[@id='OK']")

    def fill_page_name(self, page_name):
            self.pageNameTextBox.enter(page_name)

    def clear_current_page_name(self):
        self.pageNameTextBox.clear()

    def select_parent_page(self, parent_page: Page):
        if parent_page is not None:
            time.sleep(2)
            self.parentPageSelection.select_by_text(parent_page.name)

    def select_number_of_column(self, number_of_column):
        if number_of_column is not None:
            time.sleep(5)
            self.numberOfColumnSelection.select_by_text(number_of_column)

    def select_display_after(self, display_after: Page):
        if display_after is not None:
            time.sleep(2)
            self.displayAfterSelection.select_by_text(display_after.name)

    def click_on_public(self, if_public):
        if if_public:
            self.publicCheckbox.click()

    def click_on_submit_button(self):
        self.okButton.click()

    @allure.step("Edit Page Name")
    def edit_page_name(self, page: Page, new_page_name):
        page.name = new_page_name
        self.edit_page(page)

    @allure.step("Create new Page ")
    def create_new_page(self, page: Page):
        self.fill_page_name(page.name)
        self.select_parent_page(page.parent)
        self.select_number_of_column(page.number_of_columns)
        self.select_display_after(page.display_after)
        self.click_on_public(page.public)
        self.click_on_submit_button()

    @allure.step("Edit Page")
    def edit_page(self, new_page: Page):
        self.clear_current_page_name()
        self.fill_page_name(new_page.name)
        self.select_parent_page(new_page.parent)
        self.select_number_of_column(new_page.number_of_columns)
        self.select_display_after(new_page.display_after)
        self.click_on_public(new_page.public)
        self.click_on_submit_button()