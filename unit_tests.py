from selenium import webdriver
from framework.action_framework import Actions, Selector, Using, Page
from time import sleep


class Search(Page):  
    def search_for(self, text: str):
        self.actions.element_provider.driver.get('https://google.pl')
        self.actions.type_text(Selector(Using.NAME, 'q'), text)
        self.actions.submit()    


def test_google_search(actions: Actions):
    search_text = 'dr dissrespect'
    search_page = Search(actions)
    search_page.search_for(search_text)
    assert search_text in actions.element_provider.driver.title
    hello = actions.execute_js('return true;')
    assert hello.lower() == 'true'

