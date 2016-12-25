"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""
import time

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

from settings.variables_test import *
from classes import common_functions


class project_test(common_functions.functions,object):

    def setProject(self,test_number, menu_name, project_name, prefix,driver):

        self.driver = driver
        wait = WebDriverWait(self.driver, 90)

        try:

            self.driver.implicitly_wait(DELAY_HIGH)

            print "Open page: " +str(BASE_URL + MAIN_PAGE)
            self.driver.get(BASE_URL + MAIN_PAGE)
            self.driver.implicitly_wait(DELAY_FAST)
            self.FindFrame(self.driver)

            print "Find menu_name and click and button: " +str(menu_name)
            menu_name_test = wait.until(lambda driver: self.driver.find_element_by_link_text(menu_name))
            menu_name_test.click()

            self.driver.implicitly_wait(DELAY_FAST)
            button_create = wait.until(lambda driver: driver.find_element_by_id("create"))
            button_create.click()
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_name("tprojectName").clear()
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_name("tprojectName").send_keys(project_name)
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_name("tcasePrefix").clear()
            self.driver.find_element_by_name("tcasePrefix").send_keys(prefix)
            confirm_button = wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr[15]/td/div/input[3]"))
            confirm_button.click()

            # compare second word with user_type
            if self.FindElementXpath("/html/body/div[1]/p[1]",driver):
                    result = self.driver.find_element_by_xpath("/html/body/div[1]/p[1]").text
                    print "The project already exists: " +str(result.encode('UTF-8'))
                    return False
            else:
                return True

        except:
            self.PrintException()
            print "Failed class project_test, Test: ",test_number, menu_name, project_name, prefix
            time.sleep(DELAY_HIGH)
            return False
            pass