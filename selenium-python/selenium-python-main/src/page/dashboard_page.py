import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.automation import Selenium
from src.model.page import Page
from src.automation.element import Element, _driver, _waiter
from src.page.base_page import BasePage
from src.until.page_loader import PageLoader


class DashboardPage(BasePage):
    def __init__(self):
        self.header = Element.xpath("//title")
        self.loggedUser = Element.xpath("//a[@href='#Welcome']")
        self.globalSettingMenu = Element.xpath("//div[@id='main-menu']//li[@class='mn-setting']")

        self.itemsOnGlobalSettingMenuXpath = "//div[@id='main-menu']//li[@class='mn-setting']//following-sibling::li/a[text()='{}']"
        self.pageOnMenuBarXpath = "//div[@id='main-menu']//li[a[text()='{}']]"
        self.pageBesidePageOnMenuBarXpath = "//div[@id='main-menu']//li[a[text()='{}']]/following-sibling::li[1]/a[text()='{}']"

    @allure.step("Is dashboard page displayed")
    def is_displayed(self):
        PageLoader.wait_element_displayed(self.loggedUser)
        return self.loggedUser.is_displayed()

    @allure.step("Select Global Setting Menu")
    def select_global_setting_menu(self, option):
        time.sleep(5)
        itemsOnGlobalSettingMenu = Element.xpath(self.itemsOnGlobalSettingMenuXpath)
        self.globalSettingMenu.click()
        itemsOnGlobalSettingMenu.value = itemsOnGlobalSettingMenu.value.replace('{}', option, 1)
        itemsOnGlobalSettingMenu.click()

    def check_page_after(self, page1: Page, page2: Page):
        time.sleep(5)
        pageBesidePageOnMenuBar = Element.xpath(self.pageBesidePageOnMenuBarXpath)
        pageBesidePageOnMenuBar.value = pageBesidePageOnMenuBar.value.format(page1.name, page2.name)
        return pageBesidePageOnMenuBar.is_displayed()

    def hover_on_page(self, page: Page):
        time.sleep(2)
        PageLoader.wait_for_page_load()
        if page.parent is not None:
            self.hover_on_page(page.parent)
        pageOnMenuBar = Element.xpath(self.pageOnMenuBarXpath)
        pageOnMenuBar.value = pageOnMenuBar.value.replace('{}', page.name)
        pageOnMenuBar.hover()

    def click_on_page(self, page: Page):
        time.sleep(2)
        pageOnMenuBar = Element.xpath(self.pageOnMenuBarXpath)
        pageOnMenuBar.value = pageOnMenuBar.value.replace('{}', page.name)
        pageOnMenuBar.click()

    def open_page(self, page: Page):
        self.hover_on_page(page)
        self.click_on_page(page)

    def get_page_tilte(self):
        page_title = _driver().title.replace('TestArchitect ™ - ', '')
        return page_title

    @allure.step("Click on Delete link")
    def click_on_delete_link(self, page: Page):
        time.sleep(2)
        self.open_page(page)
        self.select_global_setting_menu("Delete")

    @allure.step("Delete the page")
    def delete_selected_page(self, page: Page):
        time.sleep(1)
        self.open_page(page)
        self.select_global_setting_menu("Delete")
        time.sleep(1)
        self.accept_alert()
        time.sleep(1)

    @allure.step("Check the page is deleted")
    def check_the_page_deleted(self, page: Page):
        time.sleep(2)
        pageOnMenuBar = Element.xpath(self.pageOnMenuBarXpath)
        pageOnMenuBar.value = pageOnMenuBar.value.replace('{}', page.name)
        return pageOnMenuBar.is_displayed()

