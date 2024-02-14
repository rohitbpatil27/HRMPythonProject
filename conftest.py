from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
username = "Admin"
password = "admin123"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option = Options()
    chrome_option.add_experimental_option("detach", True)  # browser won't close automatically
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@pytest.hookimpl(tryfirst=True)
def pytest_configuration(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "HRM Test Report"
