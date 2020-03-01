from abc import ABC, abstractmethod
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from framework.selector import Selector


class WebElementProvider(ABC):
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        
    @property
    def driver(self) -> WebDriver:
        return self.__driver
        
    @abstractmethod
    def find_element(self, selector: Selector, timeout: int) -> WebElement:
        pass
        
    @abstractmethod
    def find_elements(self, selector: Selector, timeout: int) -> List[WebElement]:
        pass
    

class BasicWebElementProvider(WebElementProvider):
    DEFAULT_TIMEOUT = 5

    def find_element(self, selector: Selector, timeout: int = None) -> WebElement:
        tout = timeout if timeout else self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, tout)\
            .until(ec.presence_of_element_located(selector.selector_tuple))

    def find_elements(self,
                      selector: Selector, timeout: int = None) -> List[WebElement]:
        tout = timeout if timeout else self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, tout)\
            .until(ec.presence_of_all_elements_located(selector.selector_tuple))
