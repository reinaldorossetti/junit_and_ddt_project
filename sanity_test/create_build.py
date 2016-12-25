import unittest

from ddt import ddt, data, unpack
from natsort import natsorted

from classes.login import *
from classes.language import *
from classes.create_build import *
from classes import common_functions

test_result = list_result

@ddt
class build_test_class(common_functions.functions, unittest.TestCase):

    def setUp(self):
        # navigate to the application home page
        self.base_url = BASE_URL
        self.login = loginTest()
        self.language = language()
        self.driver = ''
        self.build = create_build()

    @data(*get_data(BUILD_PATH_CSV))
    @unpack
    def test_run(self, test_number, menu_name, build_name, browser_test, language):
        for i in range(2):
            try:
                print "\nTest: ", test_number, menu_name, build_name, browser_test,language
                self.driver = self.setBrowser(browser_test)
                # 1. do login
                test_login = self.login.test_login_password_ok("admin","admin","admin",self.driver,browser_test)
                print "Login Set: " + str(test_login)
                # 2. Set Language
                language = self.language.setLanguage(test_number, language,self.driver)
                print "Language Set: " + str(language)

                # 3. Select Project
                self.driver.get(BASE_URL)
                projectSelect = self.selectProject("/html/body/div[3]/div/form/select", self.driver, u"TP:Test_Project")
                print "Project select: " +str(projectSelect)

                if not projectSelect:
                    return False

                self.result = self.build.setCreateBuild(test_number, menu_name, build_name, language, self.driver)
                print "Build set: " + str(self.result)

                if not self.result:
                    delete_test = self.delete(build_name, self.driver, TEST_BUILD_PAGE)
                    print "Delete project:" + str(delete_test)
                    self.result = self.build.setCreateBuild(test_number, menu_name, build_name, language, self.driver)
                    print "Build set: " + str(self.result)

                print "find_element: ", self.result
                if self.result:
                    self.result =  self.driver.find_element_by_link_text(build_name).text
                    print self.result, build_name
                    self.assertEqual(build_name,self.result)
                    print "Test Pass with success!"
                    time.sleep(DELAY_HIGH)
                    screenshot = self.driver.get_screenshot_as_file(SCREEN_SAVE + "_" +test_number+ "_"+ build_name\
                                                                    + "_" +browser_test+'.png')
                    print "Screenshot saved to: %s" % screenshot
                    list_result.append([test_number,"Passed"])
                    self.close_browser(self.driver)
                    return True
                else:
                    list_result.append([test_number,"Failed"])

            except (RuntimeError, TypeError, NameError):
                pass
                print "Failed! Test Number: ",test_number, build_name, browser_test
                print "Failed attempts: ", i
                if (i >= 2):
                    list_result.append([test_number,"Failed"])
                time.sleep(DELAY_HIGH)
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
                print list_result[i][0],list_result[i][1]
