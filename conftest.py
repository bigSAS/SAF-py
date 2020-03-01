import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from framework.action_framework import Actions, BasicWebElementProvider

@pytest.fixture(scope='function')
def driver():
    hub = 'http://192.168.1.84:4444/wd/hub'
    capabilities = DesiredCapabilities.CHROME.copy()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(options=options, command_executor=hub, desired_capabilities=capabilities)
    return driver

@pytest.fixture(scope='function')
def actions(driver):
    actions = Actions(BasicWebElementProvider(driver))
    yield actions
    
    actions.element_provider.driver.quit()

