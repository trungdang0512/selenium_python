import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.automation import Selenium
from src.model.page import Page
from src.automation.element import Element, _driver, _waiter
from src.page.base_page import BasePage
from src.until.PageLoader import PageLoader


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

    def click_on_page_on_menu_bar(self, page):
        time.sleep(2)
        pageOnMenuBar = Element.xpath(self.pageOnMenuBarXpath)
        pageOnMenuBar.value = pageOnMenuBar.value.replace('{}', page)
        pageOnMenuBar.click()

    @allure.step("Delete the page")
    def delete_selected_page(self, page: Page):
        time.sleep(2)
        self.click_on_page_on_menu_bar(page.name)
        self.select_global_setting_menu("Delete")
        self.accept_alert()

    @allure.step("Check the page is deleted")
    def check_the_page_deleted(self, page: Page):
        time.sleep(2)
        pageOnMenuBar = Element.xpath(self.pageOnMenuBarXpath)
        pageOnMenuBar.value = pageOnMenuBar.value.replace('{}', page.name)
        return  pageOnMenuBar.is_displayed()

