"""
Author: Reinaldo Mateus R J, Test version: 0.1
Fist Step - Imports modules, in Python code in one module gains access to the code in another module by
    the process of importing.
Second Step - create function get_data in csv file.
Third Step - create class and function specific for test.
"""

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from settings.variables_test import *


class addRemoveTestCase(object):

    def setAddTestCase(self,test_number, menu_name, project_name, prefix,driver):

        #self.test_browser = browsers()
        # url base of website
        self.base_url = BASE_URL
        self.driver = driver
        wait = WebDriverWait(self.driver, 90)

        try:
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.get(self.base_url+ MAIN_PAGE)
            self.driver.implicitly_wait(DELAY_FAST)
            menu_name_test = wait.until(lambda driver: driver.find_element_by_link_text(menu_name))
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
            if self.driver.find_elements(By.XPATH("/html/body/div[1]/p[1]")).size() > 0:
                    result = self.driver.find_element_by_xpath("/html/body/div[1]/p[1]").text
                    return result
            else:
                return True

        except (RuntimeError, TypeError, NameError):
            print "Failed! Test Number: ", menu_name, project_name, prefix
            time.sleep(DELAY_HIGH)
            pass

    def setRemoveTestCase(self,test_number, menu_name, project_name, prefix,driver):

        #self.test_browser = browsers()
        # url base of website
        self.base_url = BASE_URL
        self.driver = driver
        wait = WebDriverWait(self.driver, 90)

        try:
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.get(self.base_url+ MAIN_PAGE)
            self.driver.implicitly_wait(DELAY_FAST)
            menu_name_test = wait.until(lambda driver: driver.find_element_by_link_text(menu_name))
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
            if self.driver.find_elements(By.XPATH("/html/body/div[1]/p[1]")).size() > 0:
                    result = self.driver.find_element_by_xpath("/html/body/div[1]/p[1]").text
                    return result
            else:
                return True

        except (RuntimeError, TypeError, NameError):
            print "Failed! Test Number: ", menu_name, project_name, prefix
            time.sleep(DELAY_HIGH)
            pass