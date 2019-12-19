from datetime import datetime
from utility_classes import Priority,Severity,Status
import ctgeneratejsonfile
from ctreport_html import html_report
import os

class Session:
    _tests = []
    _report_directory_path = ""
    #_jsonfile_directory_path = ""
    _driver = None
    '''
    session_details = {
        "owner": "",
        "environment": "",
        "browser_name": "",
        "browser_version": "",
        "application_name":"",
        "os": "",
        "os_version": "",
        "test_execution_name": "",
    }
    '''
    __test_details = {}
    @staticmethod
    def start(path="../reports", driver=None, logo=None, session_details=None):
        Session.__test_details=session_details
        Session.__logo=logo
        Session.__test_details["start_time"]=datetime.now().strftime("%d-%m-%y %H:%M:%S")
        Session.__filename = datetime.now().strftime("%d_%m_%y_%H%M%S")
        Session._report_directory_path = os.path.abspath(path) + "\\" + Session.__filename + "\\"
        #Session.__jsonfile_directory_path = os.path.abspath(path) + "\\jsonfiles\\"
        os.makedirs(Session._report_directory_path)
        #if os.path.exists(Session.__jsonfile_directory_path) is not True:
        #    os.makedirs(Session.__jsonfile_directory_path)
        Session._driver=driver

    @staticmethod
    def get_test_status(testname):
        for test in Session._tests:
            if test.name == testname:
                return test.result

    @staticmethod
    def end():
        Session.__test_details["end_time"]=datetime.now().strftime("%d-%m-%y %H:%M:%S")
        Session.__test_details["duration"] = str(datetime.strptime(Session.__test_details["end_time"], '%d-%m-%y %H:%M:%S')
                                                 - datetime.strptime(Session.__test_details["start_time"], '%d-%m-%y %H:%M:%S'))
        for test in Session._tests:
            print(test._name,
                  test._id,
                  test._description,
                  test._start_time,
                  test._end_time,
                  test._duration,
                  test._result,
                  test._priority,
                  test._logs)
        print(Session.__test_details)
        #ctgeneratejsonfile.generate(Session.__test_details, Session._tests, Session.__jsonfile_directory_path + Session.__filename + ".json")
        html_report.generate(Session.__test_details, Session.__logo, Session._tests, Session._report_directory_path, Session.__filename)

class Test(Session):
    __temp_verify_id = 0
    __temp_assert_id = 0
    #test = None
    __temp_test_id = 0
    _result = ""

    def __init__(self,name,id=None,description=None,priority=Priority.HIGH):
        #self.test=test
        self._name = name
        if id is not None:
           self._id = "#" + str(id)
        else:
            Test.__temp_test_id += 1
            self._id = "#" + str(Test.__temp_test_id)
        self._description = description
        self._priority = priority
        self._start_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self._logs = []

    def finish(self):
        self._end_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self._duration = str(datetime.strptime(self._end_time, '%d-%m-%y %H:%M:%S')
                             - datetime.strptime(self._start_time, '%d-%m-%y %H:%M:%S'))

        if self._result == "":
            self._result = Status.PASS

        '''
        result = self.test.defaultTestResult()
        self.test._feedErrorsToResult(result, self.test._outcome.errors)
        
        if (len(result.errors) == 0 and
            len(result.failures) == 0 and
            self.SKIP==False and
            self.result == ""):
            self.result = Status.PASS
        elif self.SKIP == True:
            self.result = Status.SKIP
        elif self.result == Status.FAIL:
            self.result = Status.FAIL
        else:
            self.result = Status.BROKEN
            self.logs.append({
                "type": "broken",
                "error": str(result.errors[0][1]),
                "start-time": str(datetime.now().strftime("%H:%M:%S"))
            })
            print("result", type(result.errors[0][1]))
        '''
        Session._tests.append(self)

    def log(self, message):
        self._logs.append({
            "type": "log",
            "message": message,
            "start-time": datetime.now().strftime("%H:%M:%S")
        })

    def error(self, message,err=None, takesheetshot = False):
        path = None
        if takesheetshot:
            path = self.__take_failed_screenshot()
        self._logs.append({
            "type": "error",
            "message": message,
            "error": type(err).__name__,
            "screenshot": path,
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.FAIL

    def error(self, message,err=None, takesheetshot = False):
        path = None
        if takesheetshot:
            path = self.__take_failed_screenshot()
        self._logs.append({
            "type": "error",
            "message": message,
            "error": type(err).__name__,
            "screenshot": path,
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.FAIL

    def broken(self,*err):
        self._result = Status.BROKEN
        self._logs.append({
            "type": Status.BROKEN,
            "error": str(err),
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.BROKEN

    def skip(self,message):
        self._result = Status.BROKEN
        self._logs.append({
            "type": Status.SKIP,
            "message": message,
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.SKIP

    def __take_failed_screenshot(self):
        try:
            index = 1
            filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index)+".png"
            path = Session._report_directory_path + filename
            while os.path.exists(path):
                index += 1
                filename = ''.join(e for e in self._name if e.isalnum())+ "_" + str(index)+".png"
                path = Session._report_directory_path + filename
            Session._driver.save_screenshot(path)
            return filename
        except Exception as err:
            self._logs.append(
                {"type": "error",
                 "message": "CTReport error: Unable to take screenshot",
                 "error": type(err).__name__,
                 "start-time": str(datetime.now().strftime("%H:%M:%S")),
                 "screenshot":None
                 })

    def take_screenshot(self,message=None):
        index = 1
        filename=''.join(e for e in self._name if e.isalnum()) + "_" + str(index)+".png"
        path = Session._report_directory_path + filename
        while os.path.exists(path):
            index += 1
            filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index) + ".png"
            path = Session._report_directory_path + filename
        Session.__driver.save_screenshot(path)
        self._logs.append(
            {"type": "screenshot",
             "message": message,
             "path": filename,
             "start-time": str(datetime.now().strftime("%H:%M:%S"))
             })

    def assert_are_equal(self, actual, expected, description=None,onfail_screenshot=False):
        v = {"id": "#a"+str(Test.__temp_assert_id),
            "type": "assert",
             "actual": "",
             "expected": "",
             "merge": "",
             "status": "",
             "message": "",
             "screenshot": "",
             "data-type": "",
             "start-time": str(datetime.now().strftime("%H:%M:%S"))}
        Test.__temp_assert_id += 1
        if type(actual) != type(expected):
            v["actual"] = actual
            v["expected"] = expected
            v["status"] = Status.FAIL
            v["message"] = "Cannot verify objects of different type"" \
                    ""  actual: " + type(actual) + " expected: " + type(expected)
            self._result = Status.FAIL
        else:
            v["actual"] = actual
            v["expected"] = expected
            if type(actual) == dict:
                v["data-type"] = "dict"
                details = self.__verify_dict(actual, expected)
                if details[0]== False:
                    v["status"] = Status.FAIL
                    v["message"] = description
                    v["merge"] = details[1]
                    v["difference"] = details
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == list:
                v["data-type"] = "list"
                v["merge"] = [expected, actual]
                if not self.__verify_list(actual, expected):
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == tuple:
                v["data-type"] = "tuple"
                v["merge"] = [list(expected),list(actual)]
                if not self.__verify_tuple(actual, expected):
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            else:
                v["data-type"] = "others"
                if actual != expected:
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
        if onfail_screenshot:
            v["screenshot"] = self.__take_failed_screenshot()
        else:
            v["screenshot"] = None
        self._logs.append(v)
        #if v["status"]==Status.FAIL:
        #    self.test.fail("Assertion fail")

    def verify_are_equal(self, actual, expected, description=None, severity=Severity.BLOCKER, onfail_screenshot=False):
        v={"id":"#v"+str(Test.__temp_verify_id),
            "type": "verify",
           "actual": "",
           "expected": "",
           "merge": "",
           "status": "",
           "message": "",
           "screenshot": "",
           "severity":severity,
           "data-type":"",
           "start-time": str(datetime.now().strftime("%H:%M:%S"))}
        Test.__temp_verify_id+=1
        if type(actual)!=type(expected):
            v["actual"]=actual
            v["expected"] = expected
            v["status"]=Status.FAIL
            v["message"] = "Cannot verify objects of different type"" \
            ""  actual: "+type(actual)+" expected: "+type(expected)
            self._result = Status.FAIL
        else:
            v["actual"] = actual
            v["expected"] = expected
            if type(actual)== dict:
                v["data-type"]="dict"
                details=self.__verify_dict(actual, expected)
                if details[0]==False:
                    v["status"] = Status.FAIL
                    v["message"]=description
                    v["merge"] = details[1]
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual)==list:
                v["data-type"] = "list"
                v["merge"] = [expected,actual]
                if not self.__verify_list(actual, expected):
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual)==tuple:
                v["data-type"] = "tuple"
                v["merge"] = [list(expected),list(actual)]
                if not self.__verify_tuple(actual, expected):
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            else:
                v["data-type"] = "others"
                if actual!=expected:
                    v["status"] = Status.FAIL
                    v["message"] = description
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
        if onfail_screenshot:
            v["screenshot"] = self.__take_failed_screenshot()
        else:
            v["screenshot"]=None
        self._logs.append(v)

    def __verify_dict(self, actual, expected):
        merge = {}
        status = True
        for key in expected.keys():
            try:
                if actual[key] != expected[key]:
                    merge[key] = [expected[key], actual[key], "false"]
                    status = False
                else:
                    merge[key] = [expected[key], actual[key], "true"]
            except KeyError as err:
                status = False
                merge[key] = [expected[key], "null", "false"]

        v = set(actual.keys()).difference(set(expected.keys()))
        if len(v) > 0:
            status = False
            for s in v:
                merge[s] = ['null', actual[s], "false"]

        if status == False:
            return status, merge
        return status, merge

    def __verify_list(self, actual, expected):
        actual.sort()
        expected.sort()
        if actual!=expected:
            return False
        return True

    def __verify_tuple(self, actual, expected):
        actual=list(actual)
        expected=list(expected)
        actual.sort()
        expected.sort()
        if actual!=expected:
            return False
        return True