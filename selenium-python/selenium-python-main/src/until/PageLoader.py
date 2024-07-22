from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.automation import Selenium


class PageLoader:
    @staticmethod
    def wait_for_page_load(timeout=10):
        try:
            WebDriverWait(Selenium.driver.get_webdriver(), timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception as e:
            print(f"Exception occurred while waiting for page to load: {e}")

    @staticmethod
    def wait_element_displayed(Element):
        driver = Selenium.driver.get_webdriver()
        WebDriverWait(driver, 10).until(EC.visibility_of(Element))