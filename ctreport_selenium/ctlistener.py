from datetime import datetime
from ctreport_selenium.utility_classes import Priority, Severity, Status
from ctreport_selenium.ctreport_html import html_report
import os
import sys


class Session:
    _tests = []
    _report_directory_path = ""
    # _jsonfile_directory_path = ""
    _driver = None
    __test_details = {}
    __default_options = {
        "title": "Test Report",
        "logo": None,
        "show_reference": True,
        "zip_if_screenshot": False
    }

    @staticmethod
    def __validate_report_options(report_options):
        for key in Session.__default_options.keys():
            if not key in report_options.keys():
                report_options[key] = Session.__default_options[key]
            if type(report_options[key]) != type(Session.__default_options[key]):
                report_options.pop(key)
                report_options[key] = Session.__default_options[key]
        return report_options

    @staticmethod
    def start(test_name, path=os.path.abspath('.') + "/report/", driver=None, session_details=None,
              report_options=None):
        if report_options is None:
            Session.__report_options = Session.__default_options
        else:
            Session.__report_options = Session.__validate_report_options(report_options)
        Session.__test_details = session_details
        Session.__test_details["test_execution_name"] = test_name
        Session.__test_details["start_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        Session.__filename = datetime.now().strftime("%d_%m_%y_%H%M%S")
        Session._report_directory_path = os.path.abspath(path) + "\\" + Session.__filename + "\\"
        # Session.__jsonfile_directory_path = os.path.abspath(path) + "\\jsonfiles\\"
        os.makedirs(Session._report_directory_path)
        # if os.path.exists(Session.__jsonfile_directory_path) is not True:
        #    os.makedirs(Session.__jsonfile_directory_path)
        Session._driver = driver

    @staticmethod
    def set_driver(driver):
        Session._driver = driver

    @staticmethod
    def get_test_status(testname):
        for test in Session._tests:
            if test.name == testname:
                return test.result

    @staticmethod
    def end():
        if len(Session._tests) != 0:
            Session.__test_details["end_time"] = datetime.now().strftime("%d-%m-%y %H:%M:%S")
            Session.__test_details["duration"] = str(
                datetime.strptime(Session.__test_details["end_time"], '%d-%m-%y %H:%M:%S')
                - datetime.strptime(Session.__test_details["start_time"], '%d-%m-%y %H:%M:%S'))
            '''
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
            '''
            # ctgeneratejsonfile.generate(Session.__test_details, Session._tests, Session.__jsonfile_directory_path + Session.__filename + ".json")
            if len(os.listdir(Session._report_directory_path)) == 0 and Session.__report_options[
                "zip_if_screenshot"]:
                Session.__report_options["zip_if_screenshot"] = False

            html_report.generate(Session.__report_options, Session.__test_details, Session._tests,
                                 Session._report_directory_path,
                                 Session.__filename)
            if Session.__report_options["zip_if_screenshot"]:
                import shutil
                zip_path = shutil.make_archive(Session.__filename, 'zip', Session._report_directory_path)
                shutil.move(zip_path, Session._report_directory_path.split(Session.__filename)[0])
        else:
            print("Failed before test starts, No test found.")


class Test(Session):
    __temp_verify_id = 0
    __temp_assert_id = 0
    __temp_error_id = 0
    __temp_screenshot_id = 0
    # test = None
    __temp_test_id = 0
    _result = ""
    NOTBROKEN = False
    __id_li = []

    def __init__(self, name, id=None, description=None, priority=Priority.HIGH):
        # self.test=test
        self._name = name
        if id is not None:
            self._id = "#" + str(id)
        else:
            Test.__temp_test_id += 1
            self._id = "#" + str(Test.__temp_test_id)
        while self._id in self.__id_li:
            i = 1
            if "_" in self._id:
                i = int(self._id.split('_')[1])
                i = i + 1
                self._id = self._id.split('_')[0]
            self._id = self._id + "_" + str(i)
            i += 1
        self.__id_li.append(self._id)
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
        Session._tests.append(self)

    def log(self, *message):
        message = ' '.join([str(elem) for elem in message])
        self._logs.append({
            "type": "log",
            "message": message,
            "start-time": datetime.now().strftime("%H:%M:%S")
        })

    def error(self, *message, exception=None, takesheetshot=False):
        message = ' '.join(message)
        if exception is not None:
            exception = type(exception).__name__
        Test.__temp_error_id += 1
        path = None
        if takesheetshot:
            path = self.__take_failed_screenshot()
        self._logs.append({
            "id": "#e" + str(Test.__temp_error_id),
            "type": "error",
            "message": message,
            "error": exception,
            "screenshot": path,
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.FAIL

    def broken(self, *err):
        if Test.NOTBROKEN:
            pass
        else:
            self._result = Status.BROKEN
            self._logs.append({
                "type": Status.BROKEN,
                "error": str(err),
                "start-time": str(datetime.now().strftime("%H:%M:%S"))
            })
            self._result = Status.BROKEN

    def skip(self, message):
        self._result = Status.BROKEN
        self._logs.append({
            "type": Status.SKIP,
            "message": message,
            "start-time": str(datetime.now().strftime("%H:%M:%S"))
        })
        self._result = Status.SKIP

    def __take_failed_screenshot(self):
        Test.__temp_error_id += 1
        try:
            index = 1
            filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index) + ".png"
            path = Session._report_directory_path + filename
            while os.path.exists(path):
                index += 1
                filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index) + ".png"
                path = Session._report_directory_path + filename
            Session._driver.save_screenshot(path)
            return filename
        except Exception as err:
            self._logs.append(
                {
                    "id": "#e" + str(Test.__temp_error_id),
                    "type": "error",
                    "message": "CTReport error: Unable to take screenshot",
                    "error": type(err).__name__,
                    "start-time": str(datetime.now().strftime("%H:%M:%S")),
                    "screenshot": None
                })

    def take_screenshot(self, message=None):
        Test.__temp_screenshot_id += 1
        Test.__temp_error_id += 1
        try:
            index = 1
            filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index) + ".png"
            path = Session._report_directory_path + filename
            while os.path.exists(path):
                index += 1
                filename = ''.join(e for e in self._name if e.isalnum()) + "_" + str(index) + ".png"
                path = Session._report_directory_path + filename
            Session._driver.save_screenshot(path)
            self._logs.append(
                {
                    "id": "#s" + str(Test.__temp_screenshot_id),
                    "type": "screenshot",
                    "message": message,
                    "path": filename,
                    "start-time": str(datetime.now().strftime("%H:%M:%S"))
                })
        except Exception as err:
            self._logs.append(
                {
                    "id": "#e" + str(Test.__temp_error_id),
                    "type": "error",
                    "message": "CTReport error: Unable to take screenshot",
                    "error": type(err).__name__,
                    "start-time": str(datetime.now().strftime("%H:%M:%S")),
                    "screenshot": None
                })

    def assert_are_equal(self, actual, expected, description=None, onfail_screenshot=False):
        v = {"id": "#a" + str(Test.__temp_assert_id),
             "type": "assert",
             "actual": "",
             "expected": "",
             "merge": "",
             "status": "",
             "message": description,
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
                v["merge"] = details[1]
                if not details[0]:
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == list:
                v["data-type"] = "list"
                v["merge"] = [expected, actual]
                if not self.__verify_list(actual, expected):
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == tuple:
                v["data-type"] = "tuple"
                v["merge"] = [list(expected), list(actual)]
                if not self.__verify_tuple(actual, expected):
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            else:
                v["data-type"] = "others"
                if actual != expected:
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
        if onfail_screenshot and v["status"] == Status.FAIL:
            v["screenshot"] = self.__take_failed_screenshot()
        else:
            v["screenshot"] = None
        self._logs.append(v)
        if v["status"] == Status.FAIL:
            Test.NOTBROKEN = True
            sys.tracebacklimit = -1
            raise AssertionError

    def verify_are_equal(self, actual, expected, description=None, severity=Severity.MAJOR, onfail_screenshot=False):
        v = {"id": "#v" + str(Test.__temp_verify_id),
             "type": "verify",
             "actual": "",
             "expected": "",
             "merge": "",
             "status": "",
             "message": description,
             "screenshot": "",
             "severity": severity,
             "data-type": "",
             "start-time": str(datetime.now().strftime("%H:%M:%S"))}
        Test.__temp_verify_id += 1
        if type(actual) != type(expected):
            v["data-type"] = "others"
            v["actual"] = str(actual)
            v["expected"] = str(expected)
            v["merge"] = [str(expected), str(actual)]
            v["status"] = Status.BROKEN
            v["message"] = "Cannot verify objects of different type"" \
            "" Expected type: {} Actual type: {}".format(type(expected), type(actual)).replace('<', '{').replace('>',
                                                                                                                 '}')
            self._result = Status.BROKEN
        else:
            v["actual"] = actual
            v["expected"] = expected
            if type(actual) == dict:
                v["data-type"] = "dict"
                details = self.__verify_dict(actual, expected)
                v["merge"] = details[1]
                if not details[0]:
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == list:
                v["data-type"] = "list"
                v["merge"] = [expected, actual]
                if not self.__verify_list(actual, expected):
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            elif type(actual) == tuple:
                v["data-type"] = "tuple"
                v["merge"] = [list(expected), list(actual)]
                if not self.__verify_tuple(actual, expected):
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
            else:
                v["data-type"] = "others"
                if actual != expected:
                    v["status"] = Status.FAIL
                    self._result = Status.FAIL
                else:
                    v["status"] = Status.PASS
        if onfail_screenshot and v["status"] == Status.FAIL:
            v["screenshot"] = self.__take_failed_screenshot()
        else:
            v["screenshot"] = None
        self._logs.append(v)
        if v["status"] == Status.PASS:
            return True
        else:
            return False

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

        if not status:
            return status, merge
        return status, merge

    def __verify_list(self, actual, expected):
        actual.sort()
        expected.sort()
        if actual != expected:
            return False
        return True

    def __verify_tuple(self, actual, expected):
        actual = list(actual)
        expected = list(expected)
        actual.sort()
        expected.sort()
        if actual != expected:
            return False
        return True
