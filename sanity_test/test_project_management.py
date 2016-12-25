import unittest

from ddt import ddt, data, unpack
from natsort import natsorted

from classes.login import *
from classes.project import *
from classes.language import *
from classes import common_functions

test_result = list_result

@ddt
class project_test_class(common_functions.functions,unittest.TestCase):

    def setUp(self):

        self.login = loginTest()
        self.project = project_test()
        self.driver = ''
        self.language = language()

    @data(*get_data(PROJECT_PATH_CSV))
    @unpack
    def test_run(self, test_number, menu_name, project_name, prefix,browser_test,language):

        for i in range(2):
            print "\nTest: ", test_number, menu_name, project_name, prefix, browser_test,language
            self.driver = self.setBrowser(browser_test)

            test_login = self.login.test_login_password_ok("admin","admin","admin",self.driver,browser_test)
            print "Login: " + str(test_login)

            result_language = self.language.setLanguage(test_number,language, self.driver)
            print "Language Set: " + str(result_language)

            self.result = self.project.setProject(test_number, menu_name, project_name, prefix, self.driver)
            print "Project set: " + str(self.result)

            if not self.result:
                delete_test = self.delete(project_name, self.driver, TEST_PROJECT)
                self.result = self.project.setProject(test_number, menu_name, project_name, prefix, self.driver)
                print "Delete project:" + str(delete_test)

            try:
                print "Expected Result"
                # timeout five seconds
                for handle in self.driver.window_handles:
                    self.driver.switch_to_window(handle)

                self.result = self.driver.find_element_by_link_text(project_name).text
                print self.result, project_name
                if project_name == self.result:
                    self.assertEqual(project_name, self.result)
                    print "Test Pass with success!"
                    time.sleep(DELAY_HIGH)
                    screenshot = self.driver.get_screenshot_as_file(SCREEN_SAVE + "_" +test_number+ "_"+ project_name +'.png')
                    print "Screenshot saved to: %s" % screenshot
                    list_result.append([test_number,"Passed"])
                    self.close_browser(self.driver)
                    return True
                else:
                    print "error: " + self.result
                    list_result.append([test_number,"Failed"])

            except (RuntimeError, TypeError, NameError):
                print "Failed! Test Number: ",test_number, project_name
                print "Failed attempts: ", i
                if (i >= 2):
                    list_result.append([test_number,"Failed"])
                    self.close_browser(self.driver)
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
    obj = project_test_class()
