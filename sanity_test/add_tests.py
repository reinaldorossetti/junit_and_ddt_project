import unittest

from ddt import ddt, data, unpack

from classes.login import *
from classes.project import *
from classes.language import *
from classes.common_functions import *


@ddt
class test_add_test_case(unittest.TestCase,object):

    def setUp(self):
        # navigate to the application home page
        self.base_url = BASE_URL
        self.login = loginTest()
        self.project = project_test()
        self.driver = ''
        self.language = language()

    @data(*get_data(PROJECT_PATH_CSV))
    @unpack
    def test_run(self, test_number, menu_name, project_name, prefix, browser_test, language):

        wait = WebDriverWait(self.driver, 60)
        for i in range(3):

            print "\nTest: ", test_number, menu_name, project_name, prefix, browser_test,language
            self.driver = self.setBrowser(browser_test)

            # 1 Step - Do Login
            test_login = self.login.test_login_password_ok("admin","admin","admin",self.driver)
            print "login: " + str(test_login)

            # 2 Step - Set Language
            test_language = self.language.setLanguage(test_number,language, self.driver)
            print "login: " + str(test_language)

            # 3. Select Project
            self.driver.get(BASE_URL)
            projectSelect = self.selectProject("/html/body/div[3]/div/form/select", self.driver, u"TP:Test_Project")
            print "Project select: " +str(projectSelect)


            try:
                print "Test: "
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
                    return True
                else:
                    print "error: " + self.result
                    list_result.append([test_number,"Failed"])
            except:
                print "Failed! Test Number: ",test_number, project_name
                print "Failed attempts: ", i
                if (i >= 2):
                    list_result.append([test_number,"Failed"])
                    return False
                time.sleep(DELAY_HIGH)
                pass
        # Logout this web application
        self.driver.get(self.base_url+ LOGOUT_PAGE)


    def tearDown(self):
        list_result.sort()
        print "\nTest Number / Result   "
        for i in xrange(0,len(list_result)):
                print "----------------------------------"
                print list_result[i][0],list_result[i][1]
        #self.driver.close()