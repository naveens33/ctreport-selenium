import pytest
from selenium import webdriver
from ctlistener import Session
from _pytest.runner import runtestprotocol

@pytest.fixture(scope="session",autouse=True)
def driver(request):
    driver_ = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/")
    test_details = {
        "owner": "Naveen S",
        "environment": "QA",
        "browser_name": "chrome",
        "browser_version": "chrome",
        "application_name": "Zero Bank",
        "os": "Windows",
        "os_version": "10",
        "test_execution_name": "Smoke Test",
    }
    Session.start(path="\\report\\",
                  logo="D:\\delta_logo.png",
                  session_details=test_details)
    def quit():
        Session.end()
        driver_.quit()
    request.addfinalizer(quit)
    return driver_
'''
def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            print("******************",item.name,report.outcome,report.longreprtext)
    return True
'''