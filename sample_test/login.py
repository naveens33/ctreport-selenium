from ctlistener import Test, Priority, Severity
import traceback
import time

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

def test_forgot_password(driver):
    test=Test("forgot password",description="test02",priority=Priority.MEDIUM)
    try:
        test.log("test02 started")
        time.sleep(3)
        print("TestCase1.test02")
        test.log("test01 ended")
        time.sleep(2)
        raise ArithmeticError
    except Exception as err:
        test.broken(type(err).__name__,err,traceback.format_exc())
    finally:
        test.finish()
