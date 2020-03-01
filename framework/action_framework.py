from abc import ABC, abstractmethod
from enum import Enum
from typing import NamedTuple, List, Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Using(Enum):
    ID = 'id'
    NAME = 'name'
    XPATH = 'xpath'


class Selector(NamedTuple):
    using: Using
    value: str
    
    @property
    def selector_tuple(self) -> Tuple[str, str]:
        return (self.using.value, self.value)


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

    def find_elements(self, selector: Selector, timeout: int = None) -> List[WebElement]:
        tout = timeout if timeout else self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, tout)\
            .until(ec.presence_of_all_elements_located(selector.selector_tuple))


class Actions:
    def __init__(self, element_provider: WebElementProvider):
        self.__element_provider = element_provider
    
    @property
    def element_provider(self) -> WebElementProvider:
        return self.__element_provider
    
    def click(self, selector: Selector, timeout: int = None):
        self.element_provider.find_element(selector, timeout).click()
        
    def type_text(self, selector: Selector, text: str, timeout: int = None):
        self.element_provider.find_element(selector, timeout).send_keys(text)
    
    def submit(self, selector: Selector = None, timeout: int = None):
        s = selector if selector else Selector(Using.XPATH, '//form')
        self.element_provider.find_element(s, timeout).submit()
        
    def get_attribute(self, selector: Selector, attr: str, timeout: int = None) -> str:
        return self.element_provider.find_element(s, timeout).get_attribute(attr)
    
    def execute_js(self, js_script: str) -> str:
        return str(self.element_provider.driver.execute_script(js_script))


class Page(ABC):
    def __init__(self, actions: Actions):
        self.__actions = actions
    
    @property
    def actions(self) -> Actions:
        return self.__actions

