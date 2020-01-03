import pytest
from ctreport_selenium.ctlistener import Test, Priority
import traceback

@pytest.mark.run(order=2)
def test_do_login(driver):
    test = Test("Do login scenario", description="test01", priority=Priority.LOW)
    try:
        test.log("Navigated to Home page")
        signin = driver.find_element_by_id("signin_button")
        signin.click()
        test.log("Navigated to Login page")
        username = driver.find_element_by_id("user_login")
        username.send_keys("username")
        password = driver.find_element_by_id("user_password")
        password.send_keys("password")
        signin_button = driver.find_element_by_name("submit")
        signin_button.click()
        test.assert_are_equal( driver.title,"Zero - Account Summary","Unable to navigate to Account Summary page")
        test.log("Navigated successfully to Account Summary page")
    except Exception as err:
        test.broken(type(err).__name__,err,traceback.format_exc())
    finally:
        test.finish()

@pytest.mark.run(order=1)
def test_forgot_password(driver):
    test=Test("Forgot password",description="test02",priority=Priority.MEDIUM)
    try:
        test.log("Navigated to Login page")
        driver.find_element_by_xpath("//a[contains(text(),'Forgot')]").click()
        test.log("Navigated to Forgot Password page")
        driver.find_element_by_id("invalid").click()
    except Exception as err:
        test.broken(type(err).__name__,err,traceback.format_exc())
    finally:
        driver.get("http://zero.webappsecurity.com/")
        test.finish()
