import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from ctlistener import Session, Test,Severity,Priority

class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        cls.driver = webdriver.Chrome(executable_path=r'D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe')
        cls.driver.maximize_window()
        Session.start(driver=cls.driver,
                      logo="D:\\delta_logo.png",
                      session_details=test_details)


    def setUp(self):
        '''
        self.driver.get("http://zero.webappsecurity.com/index.html")
        signin = self.driver.find_element_by_id("signin_button")
        signin.click()
        username = self.driver.find_element_by_id("user_login")
        username.send_keys("username")
        password = self.driver.find_element_by_id("user_password")
        password.send_keys("password")
        self.driver.find_element_by_name("submit").click()
        #assert "Zero - Account Summary" in self.driver.title
        self.assertEqual("Zero - Account Summary",self.driver.title)
        '''

    def test_cashaccount(self):
        self.test = Test("Verify cash account link", description="Verify cash account link")
        self.test.log("Navigated to Account Summary page")
        '''
        self.driver.find_element_by_xpath("//h2[contains(text(),'Cash Accounts')]")
        self.driver.find_element_by_xpath("//tr[1]/td/a[contains(text(),'Savings')]").click()
        self.assertEqual("Zero - Account Activity",self.driver.title)
        heading=self.driver.find_element_by_xpath("//*[@id='ui-tabs-1']/h2").text
        self.assertEqual("Show Transactions",heading)
        select = Select(self.driver.find_element_by_name('accountId'))
        selectedoption=select.first_selected_option
        self.assertEqual("Savings",selectedoption.text)
        '''

    def test_creditaccount(self):
        self.test = Test("Verify credit account link", description="Verify credit account link")
        self.skipTest("I want to skip")
        self.test.log("Navigated to Account Summary page")

    def test_savingaccount(self):
        self.test = Test("Verify saving account link", description="Verify saving account link")
        self.test.log("Navigated to Account Summary page")
        raise ArithmeticError

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        x=result.errors
        pass

    @classmethod
    def tearDownClass(inst):
        Session.end()
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()