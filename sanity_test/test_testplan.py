import unittest

from ddt import ddt, data, unpack
from natsort import natsorted

from classes.login import *
from classes.browsers_test import *
from classes.create_test_plan import *
from classes.language import *
from settings.variables_test import *
from classes import common_functions

test_result = list_result

@ddt
class test_plan_class(common_functions.functions,unittest.TestCase,object):

    def setUp(self):
        self.login = loginTest()
        self.test_browser = browsers()
        self.test_plan = test_Plan()
        self.language = language()
        self.flag_language = False

    @data(*get_data(TESTPLAN_PATH_CSV))
    @unpack
    def test_run(self, test_number, menu_name, testplan_name, browser_test, language):

        print "\nTest: ",test_number, menu_name, testplan_name, browser_test, language
        self.driver = self.setBrowser(browser_test)

        test_login = self.login.test_login_password_ok("admin","admin","admin",self.driver,browser_test)
        print "Login Set: " + str(test_login)

        test_language = self.language.setLanguage(test_number,language,self.driver)
        print "Language Set: " + str(test_language)
        time.sleep(DELAY_FAST)

        #self.driver.get(BASE_URL + TEST_PLAN_PAGE)
        self.result = self.test_plan.create_test_plan(test_number, menu_name, testplan_name, self.driver)
        print "Test Plan Set: " + str(self.result)


        wait = WebDriverWait(self.driver, 90)

        if not self.result:
            self.delete(testplan_name,self.driver,TEST_PLAN_PAGE)
            self.test_plan.create_test_plan(test_number, menu_name, testplan_name, self.driver)

        time.sleep(DELAY_HIGH)
        # Try three times if fail.
        for i in range(3):
            try:
                print "Compare elements!"
                # timeout five seconds
                elem = wait.until(lambda driver: driver.find_element_by_link_text(testplan_name))
                print "find_element: ", elem.text
                if testplan_name == elem.text:
                    self.assertEqual(testplan_name, elem.text)
                    print "Test Pass with success!"
                    time.sleep(DELAY_HIGH)
                    screenshot = self.driver.get_screenshot_as_file(SCREEN_SAVE + "_" +test_number+ "_"+ testplan_name\
                                                                    + "_" +browser_test+'.png')
                    print "Screenshot saved to: %s" % screenshot
                    list_result.append([test_number,"Passed"])
                    self.driver.close()
                    return True
            except:
                self.PrintException()
                print "Failed! Test Number: ",test_number, testplan_name, browser_test
                print "Failed attempts: ", i
                if (i >= 2):
                    list_result.append([test_number,"Failed"])
                    self.driver.close()
                    return False
                time.sleep(DELAY_HIGH)
                pass
        # Logout this web application
        self.driver.get(BASE_URL + LOGOUT_PAGE)

    def tearDown(self):
        new_list = test_result
        test = natsorted(new_list, number_type=int)
        list_result = test
        print "\nTest Number / Result   "
        for i in xrange(0,len(list_result)):
                print "----------------------------------"
                print list_result[i][0],list_result[i][1]

if __name__ == '__main__':
    obj = test_plan_class()
