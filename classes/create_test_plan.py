"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""
import time

from selenium.webdriver.support.ui import WebDriverWait

from classes import common_functions as classfunctions
from settings.variables_test import *


class test_Plan(object):

    def create_test_plan(self,test_number, menu_name, testplan_name, driver):

        self.function = classfunctions.functions()
        self.driver = driver
        wait = WebDriverWait(self.driver, 90)

        try:
            self.driver.get(BASE_URL + MAIN_PAGE)
            self.driver.implicitly_wait(DELAY_HIGH)
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
                print driver.switch_to_window(handle)

            self.driver.implicitly_wait(DELAY_FAST)
            wait = WebDriverWait(self.driver, 60)
            self.driver.implicitly_wait(DELAY_FAST)
            menu_name_test = wait.until(lambda driver: self.driver.find_element_by_link_text(menu_name))
            menu_name_test.click()
            self.driver.implicitly_wait(DELAY_FAST)
            # Deleting project if exist.
            self.driver.implicitly_wait(DELAY_FAST)
            button_create = wait.until(lambda driver: driver.find_element_by_name("create_testplan"))
            button_create.click()
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_name("testplan_name").clear()
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_name("testplan_name").send_keys(testplan_name)
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_name("active").click()
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_name("is_public").click()
            confirm_button = wait.until(lambda driver: driver.find_element_by_name("do_create"))
            confirm_button.click()
            time.sleep(DELAY_HIGH)

            # compare second word with user_type
            if self.function.FindElementXpath("/html/body/div/div/p",driver):
                    result = self.driver.find_element_by_xpath("/html/body/div/div/p").text
                    print "Test Plan exists: " +str(result.encode('UTF-8'))
                    return False
            else:
                return True

        except (RuntimeError, TypeError, NameError):
            print "Failed! Test Number: ",test_number, menu_name, testplan_name
            time.sleep(DELAY_HIGH)
            return False
            pass