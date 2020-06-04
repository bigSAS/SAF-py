import pytest
from selenium import webdriver
from framework.action_framework import Actions
from framework.element_provider import BasicWebElementProvider


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def actions(driver):
    actions = Actions(BasicWebElementProvider(driver))
    yield actions
