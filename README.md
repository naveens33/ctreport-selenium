![Logo](/ctreport_selenium/ctreport_html/resource/logo.png) 

# CT Report for Selenium

ctreport-selenium is a simple, creative and customizable report for selenium automation testing using Python.

## Feature

* Different view of your test execution result
* Dashboard view with multiple graphs to understand the tests
* Test Detail view to show complete test
* Filter and Search any test
* Reference section for ctreport-selenium specific terminologies like Status, Priority, and Severity
* Customizable option through JSON file
* Screenshots better view
* Toast message for every endpoint of the report for the clear understanding
* Fairly mobile friendly

![Sample Image](ctreport_sample.gif)


### Installation and Usage

```pip install ctreport-selenium```

### Define reportconfig.json file
First, you should define the session. While creating session session_details and report_options can be defined/modified.

In session_details, you can provide the current test session details

[reportconfig.json](ctreport_selenium/reportconfig.json)

```
"session_details" : {
      "Owner": "Naveen.S",
      "application_name": "MyApp1",
      "application_version": "V1.04",
      "platform": "Windows10",
      "additional_information":"Browser - Chrome 84"
},
```

In report_options, below properties can be provided

* theme (Default/Dark Angel) (Currently ctreport-selenium supports two theme 1. Default 2. Dark Angel)
* title (report title)
* logo (your company logo)
* show_reference (reference section)
* zip_if_screenshot (In case, the screenshot is created then you can select this option to create zip file- report+screenshot )

 ```
  "report_options" :{
      "theme": "Default",
      "title": "Test Report",
      "logo": "MYLOGO.PNG",
      "show_reference": "True",
      "zip_if_screenshot": "True"
 }
 ```

**Start the Session**

```
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
Session.start(test_execution_name="Smoke Test - MyApp1",
            path="D:\\reports",
            driver=cls.driver,
            config_file=r"D:\\reportconfig.json")
```


### Create Test
For each test, you can create an object for the Test class. While creating the object for the Test class you can define the below parameters

* Name
* Id 
* Description	
* Priority (Refer below reference section)

```
test = Test("Search Fund links", 
             id=4574,
             description="Search by search term- Fund",
             priority=Priority.MEDIUM)
```

### Methods in Session class

|Method|Description|
|------|-----------|
|set_driver(driver)|In case of driver is not passes in Session.start() method later you can pass through this method|

### Methods in Test class

|Method|Description|
|------|-----------|
|log(self, \*message)|Method to record the steps for your test in the report <br> ```self.test.log("Navigate to search page")```|
|error(self, \*message, exception=None, takescreenshot=False)|Method to record the error message in the report|
|broken(self, \*err)|Method to mark the current test as Broken and record the exceptions<br> Broken - Test case stopped due to fatal errors(check the reference section)|
|skip(self, message)|Method to skip the current test|
|take_screenshot(self, message=None)|Method to take screenshot|
|assert_are_equal(self, actual, expected, description=None, onfail_screenshot=False)|Mark the assertion steps and it supports asserting following types <br> *Number* <br> *String* <br> *Boolean* <br> *Dictionary* <br> *List* <br> *Tuple* <br> **Note:** *All assertions are treated as Blocker severity* (check the reference section)|
|verify_are_equal(self, actual, expected, description=None, severity=Severity.MAJOR, onfail_screenshot=False)|Mark the verification steps and it supports verifing the following types <br> *Number* <br> *String* <br> *Boolean* <br> *Dictionary* <br> *List* <br> *Tuple* <br> (check the reference section)|



### Finish Test
Every test should be finshed before next test start/before Session ends
```
test.finish()
```

### End Sesion
Session should be end at end of your script
```
Session.end()
```

## Reference 

### Status

Status: Test status after execution

 |Status|Description|
 |------|-----------|
 |Pass |Test case is passed without any verification/assertion/fatal errors|
 |Fail|Test case is failed due to verification/assertion errors|
 |Skip|Test case skipped due to blocker or critical issue in dependencies|
 |Broken|Test case stopped due to fatal errors|
 
### Priority
 
Priority: Applies to test case

|Priority|Description|
|--------|-----------|
|High|Test case on the most important features of the application|
|Medium|Test case on features of the application which is next to High priority test cases|
|Low|Test case on features of the application which is considered to be executed rarely|

### Severity

Severity: Applies to verification and assertion statements

Note: All assertions are treated as Blocker severity

|Severity|Description|
|--------|-----------|
|Blocker|The system or functionality is currently unavailable to continue working on the application because of this incident|
|Critical|Essential functionality is not functioning and no acceptable workaround|
|Major|Essential functionality is not functioning unless acceptable workaround is implemented|
|Minor|Minor inconvenience in the functionality and application remains operational|

## Issues

If you encounter any problems, please file an issue along with a detailed description.