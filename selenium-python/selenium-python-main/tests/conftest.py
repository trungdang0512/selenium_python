# import logging
# import os
# import pytest
# from pytest_html import extras
# from src.automation import Selenium
#
# # Thiết lập logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         # logger.info("Running pytest_runtest_makereport")
#         driver = Selenium.get_webdriver()
#         if driver:
#             # Sử dụng os.path để xây dựng đường dẫn đúng
#             file_name = f"{item.nodeid.replace('::', '_')}.png"
#             screenshots_dir = os.path.join(os.getcwd(), "screenshots")
#             os.makedirs(screenshots_dir, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
#             file_path = os.path.join(screenshots_dir, file_name)
#             if driver.save_screenshot(file_path):
#                 logger.info(f"Screenshot saved to {file_path}")
#                 if hasattr(rep, 'extra'):
#                     rep.extra.append(extras.image(file_path))
#                 else:
#                     rep.extra = [extras.image(file_path)]
#             else:
#                 logger.error(f"Failed to save screenshot to {file_path}")
#
# def pytest_html_report_title(report):
#     report.title = "Test Report"
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     # logger.info("Running pytest_sessionfinish")
#     if session.config.option.htmlpath:
#         method_name = session.items[-1].name
#         new_report_path = os.path.join(os.path.dirname(session.config.option.htmlpath), f"{method_name}.html")
#         # logger.info(f"Changing report path to {new_report_path}")
#         session.config.option.htmlpath = new_report_path

import os
import pytest
import allure
from selenium import webdriver
from pytest_html import extras
from selenium.common.exceptions import NoAlertPresentException

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Đặt thư mục lưu trữ kết quả Allure
    config.option.allure_report_dir = 'allure-results'

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Lấy kết quả của mỗi bài test
    outcome = yield
    rep = outcome.get_result()

    # Nếu bài test thất bại, chụp ảnh màn hình và lưu vào báo cáo Allure và HTML
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('browser')
        if driver:
            try:
                alert = driver.switch_to.alert
                alert_text = alert.text
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
                alert.accept()
            except NoAlertPresentException:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
                file_name = f"{item.nodeid.replace('::', '_')}.png"
                screenshots_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)
                file_path = os.path.join(screenshots_dir, file_name)
                driver.save_screenshot(file_path)
                if hasattr(rep, 'extra'):
                    rep.extra.append(extras.image(file_path))
                else:
                    rep.extra = [extras.image(file_path)]

def pytest_html_report_title(report):
    report.title = "Test Report"

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if session.config.option.htmlpath:
        method_name = session.items[-1].name
        new_report_path = os.path.join(os.path.dirname(session.config.option.htmlpath), f"{method_name}.html")
        session.config.option.htmlpath = new_report_path

@pytest.hookimpl(tryfirst=True)
def pytest_unconfigure(config):
    # Chuyển đổi báo cáo Allure sang định dạng HTML
    allure_results_dir = config.option.allure_report_dir
    allure_report_dir = os.path.join(os.getcwd(), 'allure-report')
    os.system(f"allure generate {allure_results_dir} -o {allure_report_dir} --clean")
