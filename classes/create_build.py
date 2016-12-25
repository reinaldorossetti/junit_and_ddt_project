"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""
import time

from selenium.webdriver.support.ui import WebDriverWait

import classes.common_functions
from settings.variables_test import *


class create_build(classes.common_functions.functions,object):

    def setCreateBuild(self,test_number, menu_name, build_name, language, driver):

        self.driver = driver
        wait = WebDriverWait(self.driver, 90)

        try:

            #self.driver.get(BASE_URL + MAIN_PAGE)
            wait = WebDriverWait(self.driver, 60)
            self.driver.implicitly_wait(DELAY_FAST)
            # verified field  Baselines / Releases
            print "1 Click in menu name: " + str(menu_name)
            driver.switch_to_frame("mainframe");
            menu_name_test = wait.until(lambda driver: driver.find_element_by_link_text(menu_name))
            menu_name_test.click()
            self.driver.implicitly_wait(DELAY_FAST)

            print "2 Click in create_build button."
            button_create = wait.until(lambda driver: driver.find_element_by_name("create_build"))
            button_create.click()

            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_name("build_name").clear()
            self.driver.implicitly_wait(DELAY_FAST)
            print "3 Send keys build name."
            self.driver.find_element_by_id("build_name").send_keys(build_name)
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_id("is_active").click()
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_id("is_open").click()
            self.driver.implicitly_wait(DELAY_HIGH)
            self.driver.find_element_by_id("is_active").click()
            self.driver.implicitly_wait(DELAY_FAST)
            self.driver.find_element_by_id("is_open").click()
            self.driver.implicitly_wait(DELAY_FAST)
            print "4 Select time today"
            confirm_button = wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr[5]/td/img[1]"))
            confirm_button.click()
            time.sleep(DELAY_FAST)
            confirm_button = wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div/div/form/table/tbody/tr[5]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/em/button"))
            confirm_button.click()
            time.sleep(DELAY_FAST)
            confirm_button = wait.until(lambda driver: driver.find_element_by_name("do_create"))
            confirm_button.click()

            print "find message error or continue!"

            # compare second word with user_type
            if self.FindElementXpath("/html/body/div/div/p",driver):
                    result = self.driver.find_element_by_xpath("/html/body/div/div/p").text
                    print "Test Plan exists: " +str(result.encode('UTF-8'))
                    return False
            else:
                return True

        except (RuntimeError, TypeError, NameError):
            print "Failed! Test Number: ",test_number, menu_name, build_name
            time.sleep(DELAY_HIGH)
            return False
            pass