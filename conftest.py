import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from framework.action_framework import Actions
from framework.element_provider import BasicWebElementProvider


LOCAL_WEBDRIVER = False

HUB_URL = 'http://sas-kodzi.pl:4444/wd/hub'
PING_TIMEOUT = 5


@pytest.fixture(scope='session')
def hub_is_online():
    try:
        response = requests.get(
            HUB_URL.replace('wd/hub', 'grid/api/hub'),
            timeout=PING_TIMEOUT
        )
        return response.status_code == 200
    except requests.ConnectionError as e:
        return False


@pytest.fixture(scope='function')
def driver(hub_is_online):
    if not LOCAL_WEBDRIVER:
        if not hub_is_online:
            raise Exception("Selenium HUB is offline :(")
        
        capabilities = DesiredCapabilities.CHROME.copy()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        return webdriver.Remote(
            command_executor=HUB_URL,
            options=options,
            desired_capabilities=capabilities
        )
    else:
        return webdriver.Chrome()


@pytest.fixture(scope='function')
def actions(driver):
    actions = Actions(BasicWebElementProvider(driver))
    yield actions
    
    actions.element_provider.driver.quit()
