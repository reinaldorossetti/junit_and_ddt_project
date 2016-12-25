"""
Author: Reinaldo Mateus R J, Test version: 0.1
Fist Step - Imports modules, in Python code in one module gains access to the code in another module by
    the process of importing.
Second Step - create function get_data in csv file.
Third Step - create class and function specific for test.
"""

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from settings.variables_test import *
import classes.common_functions


class loginTest(classes.common_functions.functions,object):

    def test_login_password_ok(self,tl_login,tl_password,user_type,driver,browser_type):

        #self.test_browser = browsers()
        # url base of website
        self.base_url = BASE_URL
        self.driver = driver
        wait = WebDriverWait(self.driver, 90)
        time.sleep(4)

        try:
            self.driver.get(self.base_url+ LOGIN_PAGE)

            elem = wait.until(lambda driver: driver.find_element_by_name("tl_login"))
            # Send user name in tl_login field
            elem.send_keys(tl_login)
            # Next we are sending keys, this is similar to entering keys using your keyboard.
            elem.send_keys(Keys.RETURN)
            elem = self.driver.find_element_by_name("tl_password")
            # Send password in tl_password field
            elem.send_keys(tl_password)
            # This is similar to entering keys using your keyboard.
            elem.send_keys(Keys.RETURN)
            time.sleep(DELAY_FAST)
            # timeout five seconds
            time.sleep(DELAY_FAST)
            self.driver.get(self.base_url+ MAIN_MENU)
            print "\nTest: ", tl_login, tl_password, user_type, browser_type
            time.sleep(DELAY_FAST)
            confirm = wait.until(lambda driver: driver.find_element_by_xpath\
                ("/html/body/div[2]/span[contains(text(),'"+user_type+"')]" ))
            print  confirm.text
            elem_test = str(confirm.text)
            time.sleep(DELAY_FAST)
            # split text in two words in the string.
            elem_test = elem_test.split(" ", 1)
            time.sleep(DELAY_FAST)
            print "Tag value: " + str(elem_test)
            # compare second word with user_type
            if elem_test[1] == "["+user_type+"]":
                    time.sleep(DELAY_FAST)
                    return elem_test[1]
            else:
                return False

        except (RuntimeError, TypeError, NameError):
            pass
            print "Failed! Test Number: ", tl_login, tl_password, user_type
            time.sleep(DELAY_HIGH)
            return False