# CT Report for Selenium

ctreport for selenium automation will provide simple and creative html file for day to day software testing

### Installation and Usage

```pip install ctreport-selenium```

### Define Session 

First you should define the session. While creating session session_details and report options should be provided.

In session_details, you can provide the current test session details

```
session_details = {
            "owner": "Naveen.S",
            "application": "MyApp1",
            "application version": "V1.04",
            "os": "Windows10",
            "browser": "Chrome"
        }
```

In report_options, below propeties can be provided

* title (report title)
* logo (your company logo)
* show_reference (reference section)
* zip_if_screenshot (In case, the screenshot is created then you can select this option to create zip file- report+screenshot )

 ```
 report_options = {
            "title": "Test Report",
            "logo": r"D:\MYLOGO.PNG",
            "show_reference": True,
            "zip_if_screenshot": True
        }
 ```
