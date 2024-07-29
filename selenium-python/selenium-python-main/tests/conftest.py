# # import logging
# # import os
# # import pytest
# # from pytest_html import extras
# # from src.automation import Selenium
# #
# # # Thiết lập logging
# # logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)
# #
# # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     rep = outcome.get_result()
# #     if rep.when == "call" and rep.failed:
# #         # logger.info("Running pytest_runtest_makereport")
# #         driver = Selenium.get_webdriver()
# #         if driver:
# #             # Sử dụng os.path để xây dựng đường dẫn đúng
# #             file_name = f"{item.nodeid.replace('::', '_')}.png"
# #             screenshots_dir = os.path.join(os.getcwd(), "screenshots")
# #             os.makedirs(screenshots_dir, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
# #             file_path = os.path.join(screenshots_dir, file_name)
# #             if driver.save_screenshot(file_path):
# #                 logger.info(f"Screenshot saved to {file_path}")
# #                 if hasattr(rep, 'extra'):
# #                     rep.extra.append(extras.image(file_path))
# #                 else:
# #                     rep.extra = [extras.image(file_path)]
# #             else:
# #                 logger.error(f"Failed to save screenshot to {file_path}")
# #
# # def pytest_html_report_title(report):
# #     report.title = "Test Report"
# #
# # @pytest.hookimpl(tryfirst=True)
# # def pytest_sessionfinish(session, exitstatus):
# #     # logger.info("Running pytest_sessionfinish")
# #     if session.config.option.htmlpath:
# #         method_name = session.items[-1].name
# #         new_report_path = os.path.join(os.path.dirname(session.config.option.htmlpath), f"{method_name}.html")
# #         # logger.info(f"Changing report path to {new_report_path}")
# #         session.config.option.htmlpath = new_report_path
import os
import pytest
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Đặt thư mục lưu trữ kết quả Allure
    if not hasattr(config.option, 'allure_report_dir'):
        config.option.allure_report_dir = 'allure-results'
    allure_results_dir = config.option.allure_report_dir
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

@pytest.hookimpl(tryfirst=True)
def pytest_unconfigure(config):
    # Chuyển đổi báo cáo Allure sang định dạng HTML
    allure_results_dir = config.option.allure_report_dir
    allure_report_dir = os.path.join(os.getcwd(), 'allure-report')
    logger.info(f"Generating Allure report to: {allure_report_dir}")

    # Sử dụng lệnh allure generate
    result = os.system(f"allure generate {allure_results_dir} -o {allure_report_dir} --clean")
    if result != 0:
        logger.error(f"Failed to generate Allure report with exit code {result}")
        return

    # Kiểm tra nếu thư mục allure-report được tạo và có file index.html
    if os.path.exists(os.path.join(allure_report_dir, 'index.html')):
        logger.info(f"Allure report successfully generated at: {allure_report_dir}")
    else:
        logger.error("Failed to generate Allure report")

# Chạy kiểm thử và lưu kết quả vào thư mục Allure
if __name__ == "__main__":
    pytest.main(["--alluredir=allure-results"])