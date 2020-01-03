import pytest
from selenium.webdriver.common.keys import Keys
from ctlistener import Test, Priority, Severity

class Test_Search():

    driver = None

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setupclass(cls, driver):
        Test_Search.driver = driver

    @pytest.mark.run(order=2)
    def test_account(self):
        self.test = Test("Search by search term- Account", description="Search by search term- Account")
        self.test.log("Navigated to Home page")
        self.driver.find_element_by_id("searchTerm").send_keys("Account")
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        self.test.log("Navigate to search page")

    @pytest.mark.run(order=1)
    def test_map(self):
        self.test = Test("Search by search term- Map", description="Search by search term- Map",priority=Priority.MEDIUM)
        self.test.log("Navigated to Home page")
        self.driver.find_element_by_id("searchTerm").send_keys("Map")
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        self.test.log("Navigate to search page")
        self.driver.find_element_by_id("invalid")
        self.test.log("Verified successfully")

    def test_money(self):
        self.test = Test("Search by search term- Money", description="Search by search term- Money",priority=Priority.MEDIUM)
        self.test.log("Navigated to Home page")
        self.driver.find_element_by_id("searchTerm").send_keys("Money")
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        self.test.log("Navigate to search page")
        expected = {"part": "1234", "sno": "2", "xno": "23"}
        actual = {"part": "1234", "sno": "1", "color": "ffff78"}
        self.test.verify_are_equal(actual, expected, "mismtach of dict", Severity.MAJOR, True)
        self.test.verify_are_equal("Map","Account","Incorrect result",Severity.MAJOR,True)

    def test_fund(self):
        self.test = Test("Search by search term- Fund", description="Search by search term- Fund",priority=Priority.MEDIUM)
        self.test.log("Navigated to Home page")
        self.driver.find_element_by_id("searchTerm").send_keys("Fund")
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        self.test.verify_are_equal((13,43,65),(13,43,65),severity=Severity.MINOR)
        self.test.log("Navigate to search page")
        self.test.assert_are_equal("Map","Account","Incorrect result",True)

    def test_account1(self):
        self.test = Test("Search by search term- Account1", description="Search by search term- Account1",priority=Priority.MEDIUM)
        pytest.skip("I want to skip")
        self.test.log("Navigated to Home page")
        self.driver.find_element_by_id("searchTerm").send_keys("Account1")
        self.driver.find_element_by_id("searchTerm").send_keys(Keys.ENTER)
        self.test.log("Navigate to search page")

    def teardown_method(self, method):
        Test_Search.test=self.test
