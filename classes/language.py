__author__ = 'Reinaldo Mateus Rossetti Junior'
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

from settings.variables_test import *
import classes.common_functions as classfunctions


class language(object):

    def setLanguage(self, test_number,language,driver):

        self.function = classfunctions.functions()

        try:
            print(language)
            self.base_url = BASE_URL
            wait = WebDriverWait(driver, 60)
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
                
            print("Click in button my settings")
            button_language = wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[2]/span[2]/a[1]/img"))
            button_language.click()
            #change frame
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
                print driver.switch_to_window(handle)

            print "select language: " +str(language)

            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,\
                                            "/html/body/div/form[1]/table/tbody/tr[5]/td/select")))
            if element:
                Select(driver.find_element_by_xpath("/html/body/div/form[1]/table/tbody/tr[5]/td/select"))
                select = Select(driver.find_element_by_xpath("/html/body/div/form[1]/table/tbody/tr[5]/td/select"))
                # select by visible text
                select.select_by_visible_text(language)
                print driver.find_element_by_xpath("/html/body/div/form[1]/table/tbody/tr[5]/td/select").text
            else:
                print("Not found the field Language!")
                return False

            if driver.find_element_by_xpath("/html/body/div/form[1]/div/input"):
                    time.sleep(DELAY_HIGH)
                    driver.find_element_by_xpath("//div/input").click()
                    button_save = driver.find_element_by_xpath("/html/body/div/form[1]/div/input").click()
                    print "Change language with success!"
                    return True
            else:
                print "Test failed!"
                return False

        except:
            self.function.PrintException()
            print("Failed! Test Number: ", test_number, language)
            return False
