__author__ = 'Reinaldo Mateus Rossetti Junior'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class browsers(object):

    def setBrowser(self,browser):

        if browser == "FIREFOX":
            #Running Standalone Selenium Server for use with RemoteDrivers, port 4441
            WEB_DRIVER = webdriver.Remote(command_executor='http://172.16.133.1:5558/wd/hub',
                   desired_capabilities=DesiredCapabilities.FIREFOX)
            return WEB_DRIVER

        elif browser == "CHROME":
            WEB_DRIVER = webdriver.Remote(command_executor='http://172.16.133.1:5555/wd/hub',
                   desired_capabilities=DesiredCapabilities.CHROME)
            return WEB_DRIVER

        elif browser == "IE":
            WEB_DRIVER = webdriver.Remote(command_executor='http://172.16.133.1:5556/wd/hub',
                   desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            return WEB_DRIVER