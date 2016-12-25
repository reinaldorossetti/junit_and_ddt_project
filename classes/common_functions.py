__author__ = 'Reinaldo M. R. Junior'
from time import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import linecache
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from settings.variables_test import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from SendKeys import SendKeys
from selenium import webdriver
from selenium.webdriver.chrome.service import *

class functions(object):


    def setBrowser(self,browser):

        if browser == "FIREFOX":
            #Running Standalone Selenium Server for use with RemoteDrivers, port 4441
            WEB_DRIVER = webdriver.Remote(command_executor='http://127.0.0.1:5557/wd/hub',
                   desired_capabilities=DesiredCapabilities.FIREFOX)
            return WEB_DRIVER

        elif browser == "CHROME":


            WEB_DRIVER = webdriver.Remote(command_executor='http://127.0.0.1:5555/wd/hub',
                   desired_capabilities=DesiredCapabilities.CHROME)
            return WEB_DRIVER

        elif browser == "IE":
            WEB_DRIVER = webdriver.Remote(command_executor='http://127.0.0.1:5556/wd/hub',
                   desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            return WEB_DRIVER

    def close_browser(self,driver):
        driver.close()
        driver.quit()


    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

    def FindFrame(self,driver):
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
            print driver.switch_to_window(handle)

    def FindElementXpath(self,elem,driver):
        from selenium.webdriver.support import expected_conditions as EC
        print "FindElementXpath"
        #self.FindFrame(driver)
        try:
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, elem)))
            if element:
                print "Element is present!"
                return True
            else:
                print "Element not found!"
                return False
        except:
            print "Except Element not found!"
            return False
            pass

    def presence_of_element_located(self,elem,driver):

        from selenium.webdriver.support import expected_conditions as EC

        try:
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, elem)))
            if element:
                print "Element is present: " +str(element)
                return True
            else:
                print "Element not found: " +str(element)
                return False
        except:
            print "Except Element not found!"
            return False


    def delete(self,test_name, driver, URL_NAME):

        if URL_NAME == TEST_PROJECT:
            driver.get(BASE_URL + TEST_PROJECT)
        elif URL_NAME == TEST_PLAN_PAGE:
            driver.get(BASE_URL + TEST_PLAN_PAGE)
        elif URL_NAME == TEST_BUILD_PAGE:
            driver.get(BASE_URL + TEST_BUILD_PAGE)

        for handle in driver.window_handles:
              driver.switch_to_window(handle)
        try:
            wait = WebDriverWait(driver, 5)
            if wait.until(lambda driver: driver.find_element_by_link_text(test_name)):
                print "project exits ok"
                # delete project send request
                link = driver.find_element_by_link_text(test_name)
                linkLocatin = link.get_attribute("href")
                print ("Link Location "+linkLocatin)

                if URL_NAME == TEST_PROJECT:
                    linkLocatin=linkLocatin.split("ID=",1)
                else:
                    linkLocatin=linkLocatin.split("id=",1)

                print "delete project id:" +str(linkLocatin[1])
                if URL_NAME == TEST_PROJECT:
                    driver.get(BASE_URL + DELETE_PROJECT+str(linkLocatin[1]))
                elif URL_NAME == TEST_PLAN_PAGE:
                    driver.get(BASE_URL + DELETE_TESTPLAN+str(linkLocatin[1]))
                elif URL_NAME == TEST_BUILD_PAGE:
                    driver.get(BASE_URL + DELETE_BUILD+str(linkLocatin[1]))

                sleep(DELAY_FAST)
                return True

        except:
            self.PrintException()
            print "Failed delete project!"
            return False
            pass
        return False

    def selectProject(self, elem, driver, select_elem):
        try:
            print "Select Project"
            sleep(DELAY_FAST)
            #element = self.FindElementXpath(elem,driver)
            self.FindFrame(driver)
            #self.frame_search(elem,driver)
            element = True
            if element:
                ## Give time for iframe to load ##
                sleep(3)
                ## You have to switch to the iframe like so: ##
                print "find element"
                # move into the iframe
                driver.switch_to_frame("titlebar");
                ## Insert text via xpath ##
                print "find xpath" +str(elem)

                select = driver.find_element_by_name("testproject")
                for option in select.find_elements_by_tag_name('option'):
                    print option.text
                    if option.text == select_elem:
                        option.click()
                        driver.switch_to_default_content()
                        return True

            else:
                print "Not found the field project!"
                return False
            ## Switch back to the "default content" (that is, out of the iframes) ##
            driver.switch_to_default_content()

        except:
            print "Except Not found the field project!"
            return False
            pass


    def size_maxi(self,driver):

        print driver.get_window_size()

        # set window size
        #driver.set_window_size(480, 320)
        #print driver.get_window_size()

        # maximize window
        driver.maximize_window()
        print driver.get_window_size()


    def size_mini(self, driver):
            actionChain = ActionChains(driver).key_down(Keys.ALT)
            actionChain.send_keys(Keys.SPACE)
            actionChain.send_keys("n")
            actionChain.perform()


    def sendKeysWindows(self,driver):

            #https://github.com/zvodd/sendkeys-py-si/blob/master/doc/SendKeys.txt
            # The object must be selected
            sleep(5)
            SendKeys("""
                {F6}
                {PAUSE 1}
                www.google.com
                {PAUSE 1}
                %{ENTER}
            """)

    def getCurrentTime(self):
        """ Return the actual date-time string-formated. """
        import datetime
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d_%Hh%Mm%S")

    def getDuration(self, star_time):

        # star_time = mktime(localtime())

        try:

            from datetime import datetime, timedelta
            self.time_atual = mktime(localtime())
            time_diff = (self.time_atual-star_time)
            time_diff = timedelta(seconds=int(time_diff))
            d = datetime(1,1,1) + time_diff
            print("DAYS:HOURS:MIN")
            #print("%d:%d:%d" % (d.day-1, d.hour, d.minute))
            duration = ("%d:%d:%d" % (d.day-1, d.hour, d.minute))
            print duration
            h = d.hour + d.minute / 60
            print "Horas: " + str(h)
        except:
            print "Erro in GetDuration"
            pass
        return duration


    def internet_on(self):
        import urllib2
        try:
            response=urllib2.urlopen('http://www.google.com',timeout=3)
            print response
            return True
        except urllib2.URLError as err:
            return False
        return False

if __name__=='__main__':
    obj = functions()
    print obj.internet_on()