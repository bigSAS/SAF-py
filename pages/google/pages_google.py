from framework.action_framework import Page, Selector, Using
from framework.conditions import XpathExists


class Search(Page):
    """Szukaj w guglu"""
    def search_for(self, text: str):
        """ wykonaj search - text: fraza jaka trza wpisac w search """
        self.actions.element_provider.driver.get('https://google.pl')
        self.actions.type_text(Selector(Using.NAME, 'q'), text)
        self.actions.submit()
        self.actions.wait_for(XpathExists("//div[@class='g']"))
