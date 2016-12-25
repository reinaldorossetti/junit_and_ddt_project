"""
Author: Reinaldo Mateus R J, Test version: 0.1
Class LoginTestClass - class to test login feature, used data driver test.
"""
import unittest
from ddt import ddt, data, unpack
from natsort import natsorted
from classes import common_functions
from classes.login import *
from settings.variables_test import *
test_result = list_result
from ctypes import *
from report.excel_report import *

# DDT consists of a class decorator @ddt (for your TestCase subclass)
@ddt
class LoginTestClass(common_functions.functions, unittest.TestCase):

    def setUp(self):

        self.login = loginTest()

    # Read the users in rows, and Passing variables tl_login,tl_password,user_type to function test_run.
    @data(*get_data(PATH_TEST_OK))
    # will automatically unpack tuples and lists into multiple arguments, and dictionaries into multiple
    # keyword arguments.
    @unpack
    def test_login_password_ok(self,test_number,test_name,tl_login,tl_password,user_type,browser_type):

        # Try three times if fail.
        for i in range(3):
            self.driver = self.setBrowser(browser_type)

            try:
                elem_test = self.login.test_login_password_ok(tl_login,tl_password,user_type,self.driver,browser_type)
                print "Login: " + str(elem_test)

                if elem_test == "["+user_type+"]":
                    if (self.FindElementXpath(XPATH_TOP_TEXT_MAIN_PAGE,self.driver)):
                        # Test - compare text expected with XPATH_TOP_TEXT_MAIN_PAGE in browser.
                        self.assertTrue((self.driver.find_element_by_xpath(XPATH_TOP_TEXT_MAIN_PAGE).text\
                                         == TOP_TEXT_MAIN_PAGE))
                        print "Test User " +user_type+ " Passed with success! Test Number: ", test_number
                        self.driver.get(BASE_URL + INDEX_MENU)
                        sleep(DELAY_FAST)
                        screenshot = self.driver.get_screenshot_as_file(SCREEN_SAVE + tl_login + "_" + tl_password +\
                                                                        "" + user_type +'.png')
                        print "Screenshot saved to: %s" % screenshot
                        list_result.append([test_number,"Passed"])
                        self.close_browser(self.driver)
                        return True
                    else:
                        # Inform if not found the field expected.
                        sleep(DELAY_HIGH)
                        list_result.append([test_number,test_name,"Failed"])
            except:
                self.PrintException()
                pass
                print "Failed! Test Number: ",test_number, tl_login, tl_password, user_type, browser_type
                print "Failed attempts: ", i
                if (i >= 2):
                    list_result.append([test_number,test_name,"Failed"])
                sleep(DELAY_HIGH)
                self.close_browser(self.driver)

        # Logout this web application
        self.driver.get(BASE_URL + LOGOUT_PAGE)


    def tearDown(self):
        new_list = test_result
        test = natsorted(new_list, number_type=int)
        list_result = test
        print "\nTest Number / Result   "
        for i in xrange(0,len(list_result)):
                print "----------------------------------"
                print list_result[i][0],list_result[i][1],list_result[i][2]


    @classmethod
    def tearDownClass(cls):
        print ""
        report = report_excel()
        report.create_excel(list_result)

if __name__ == '__main__':
    obj = LoginTestClass()
    report = report_excel()
    report.create_excel(list_result)
